from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import ssl
import boto3
import json

def get_db_credentials(secret_name, region_name):
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    except Exception as e:
        raise RuntimeError(f"Error fetching secret: {e}")

# Usage
secret_name = "myapp/db_credentials"
region_name = "us-east-1"  # Change to your region
creds = get_db_credentials(secret_name, region_name)

username = creds['username']
password = creds['password']
aws_url = creds['host']
database = creds['database']

if not all([username, password, aws_url, database]):
    raise ValueError("Missing one or more environment variables for the database connection.")

# Async database URL (no sslmode in the URL)
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@{aws_url}/{database}"

# SSL context for asyncpg
ssl_context = ssl.create_default_context()

# Create async engine with SSL
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context},
)

# Async sessionmaker
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for ORM models
Base = declarative_base()

# Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session  # Automatically handles session cleanup