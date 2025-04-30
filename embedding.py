import boto3
import json
import os
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

# --- Configuration ---
AWS_REGION = "us-east-1"  # Replace with your AWS region
BEDROCK_MODEL_ID = "amazon.titan-embed-text-v1"
# IMPORTANT: Use the Collection Endpoint URL from Phase 2
OPENSEARCH_COLLECTION_ENDPOINT = "https://jumud3coizfqh7wcw2eh.us-east-1.aoss.amazonaws.com" # Replace with your Collection Endpoint URL
OPENSEARCH_INDEX_NAME = "instruction4" # The index name you used in the PUT mapping command

# --- Authentication ---
# OpenSearch Serverless uses IAM authentication defined by Data Access Policies.
# We use AWSV4SignerAuth with the 'aoss' service name.
# Ensure the IAM user/role running this script is listed in the Data Access Policy
# for the collection and has necessary permissions (e.g., WriteDocument).
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, AWS_REGION, 'aoss') # Use 'aoss' for Serverless

# --- File Paths ---
INSTRUCTION_FILE = "Instruction.txt"
DOMAIN_FILE = "Domain.txt"
FILES_TO_PROCESS = {
    INSTRUCTION_FILE: "instruction",
    DOMAIN_FILE: "domain_knowledge"
}

# --- Initialize Clients ---
bedrock_runtime_client = boto3.client(
    service_name='bedrock-runtime',
    region_name=AWS_REGION
)

opensearch_client = OpenSearch(
    # Provide the Collection Endpoint URL
    hosts=[{'host': OPENSEARCH_COLLECTION_ENDPOINT, 'port': 443}],
    # Use AWSV4SignerAuth configured for 'aoss'
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    pool_maxsize=20
)

# --- Helper Functions ---

def get_embedding_from_bedrock(text_input):
    """Calls Bedrock to get embedding for the given text."""
    try:
        body = json.dumps({"inputText": text_input})
        response = bedrock_runtime_client.invoke_model(
            body=body,
            modelId=BEDROCK_MODEL_ID,
            accept='application/json',
            contentType='application/json'
        )
        response_body = json.loads(response['body'].read())
        embedding = response_body['embedding']
        print(f"Generated embedding for text snippet: {text_input[:80]}...")
        return embedding
    except Exception as e:
        print(f"Error getting embedding from Bedrock: {e}")
        raise

def index_document_in_opensearch(doc_id, text, embedding, source_file_tag):
    """Indexes a document (text + embedding) into OpenSearch Serverless Collection."""
    document = {
        'text_embedding': embedding,
        'text': text,
        'source_file': source_file_tag
    }
    try:
        response = opensearch_client.index(
            index=OPENSEARCH_INDEX_NAME,
            body=document,
            id=doc_id,
            refresh='wait_for' # Use 'wait_for' for testing, remove for bulk indexing performance
        )
        print(f"Indexed document ID: {doc_id}, Source: {source_file_tag}, Response: {response['result']}")
        return response
    except Exception as e:
        print(f"Error indexing document ID {doc_id} into OpenSearch: {e}")
        # Check Data Access Policy permissions if you get authorization errors
        return None

# Be conservative to be safe.
MAX_CHUNK_LENGTH_CHARS = 8192

def process_chunk(chunk_text, source_tag, base_filename, chunk_index):
    """Processes a single chunk: gets embedding and indexes it."""
    embedding = get_embedding_from_bedrock(chunk_text)
    # Consider making doc_id generation more robust if needed
    doc_id = f"{source_tag}_{base_filename}_{chunk_index}"
    index_document_in_opensearch(doc_id, chunk_text, embedding, source_tag)

def split_and_process_chunk(long_chunk, source_tag, base_filename, chunk_index_prefix):
    """Further splits a long chunk (e.g., by single newline) and processes sub-chunks."""
    sub_chunks_processed = 0
    # Simple secondary split: by single newline. Could use sentence splitter too.
    sub_chunks = long_chunk.split("\n")
    for j, sub_chunk in enumerate(sub_chunks):
        clean_sub_chunk = sub_chunk.strip()
        if not clean_sub_chunk:
            continue
        if len(clean_sub_chunk) > MAX_CHUNK_LENGTH_CHARS:
            print(f"Warning: Sub-chunk {chunk_index_prefix}.{j} still too long ({len(clean_sub_chunk)} chars), skipping.")
            continue
        try:
            print(f"Processing sub-chunk {chunk_index_prefix}.{j}, length: {len(clean_sub_chunk)} chars")
            # Use a modified index/ID for sub-chunks
            process_chunk(clean_sub_chunk, source_tag, base_filename, f"{chunk_index_prefix}.{j}")
            sub_chunks_processed += 1
        except Exception as sub_chunk_error:
            print(f"Skipping sub-chunk {chunk_index_prefix}.{j} due to error: {sub_chunk_error}")
            continue
    return sub_chunks_processed


def process_file(filepath, source_tag):
    """Reads a file, splits it into semantic chunks, handles oversized chunks, gets embeddings, and indexes them."""
    print(f"\n--- Processing file: {filepath} ---")
    doc_counter = 0
    base_filename = os.path.basename(filepath) # Get filename for IDs

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading {filepath}: {e}")
        return

    # Split on double newlines — good for instruction blocks/paragraphs
    chunks = content.strip().split("\n\n")

    for i, chunk in enumerate(chunks):
        clean_chunk = chunk.strip()
        if not clean_chunk:
            continue

        if len(clean_chunk) <= MAX_CHUNK_LENGTH_CHARS:
            # Process chunk directly if within limits
            try:
                print(f"Processing chunk {i}, length: {len(clean_chunk)} characters")
                process_chunk(clean_chunk, source_tag, base_filename, str(i))
                doc_counter += 1
            except Exception as inner_e:
                print(f"Skipping chunk {i} due to error: {inner_e}")
                continue
        else:
            # Chunk is too long, try splitting it further
            print(f"Warning: Chunk {i} is too long ({len(clean_chunk)} chars). Attempting to split further...")
            sub_chunks_indexed = split_and_process_chunk(clean_chunk, source_tag, base_filename, str(i))
            doc_counter += sub_chunks_indexed
            if sub_chunks_indexed == 0:
                 print(f"Warning: No processable sub-chunks found for oversized chunk {i}.")


    print(f"--- Finished processing {filepath}. Indexed approximately {doc_counter} documents/sub-documents. ---")



# --- Main Execution ---
if __name__ == "__main__":
    if not os.path.exists(INSTRUCTION_FILE) or not os.path.exists(DOMAIN_FILE):
       print(f"Error: Ensure '{INSTRUCTION_FILE}' and '{DOMAIN_FILE}' exist in the same directory as the script.")
    else:
        # Verify OpenSearch connection (optional but helpful)
        try:
            if not opensearch_client.ping():
                 print("Warning: Could not ping OpenSearch Serverless Collection endpoint.")
            else:
                 print("Successfully connected to OpenSearch Serverless Collection.")
        except Exception as ping_err:
            print(f"Error pinging OpenSearch Serverless: {ping_err}. Check endpoint and permissions.")
            # Optionally exit if connection fails critically
            # exit()

        for file_path, tag in FILES_TO_PROCESS.items():
            process_file(file_path, tag)

        print("\nEmbedding and indexing process complete.")