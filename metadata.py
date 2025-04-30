schema = {
    "table_name": "new_data",
    "table_schema_details":[
                                {
                                "column_name": "id",
                                "business_name": "ID",
                                "column_description": "Key for individual data entries",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "start_year",
                                "business_name": "Start Year",
                                "column_description": "Start year of model from which data is saved",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "start_month",
                                "business_name": "Start Month",
                                "column_description": "Start month of model from which data is saved",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "start_year_reporting",
                                "business_name": "Start Year Reporting",
                                "column_description": "Year of model from which data started reporting",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "start_month_reporting",
                                "business_name": "Start Month Reporting",
                                "column_description": "Month of model from which data started reporting",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "input_output",
                                "business_name": "Input/Output",
                                "column_description": "Flag to identify whether the data is a user input or based on model calculations",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "for_reporting",
                                "business_name": "Flag reporting",
                                "column_description": "Flag to check if the data is valid/available for reporting",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "is_historical",
                                "business_name": "Flag historical",
                                "column_description": "Flag to check if the data is historical",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "for_scenario_comparison",
                                "business_name": "Flag scenario comparison",
                                "column_description": "Flag to check if the data is valid/available for scenario comparison",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "non_business_row_checks",
                                "business_name": "?",
                                "column_description": "?",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_1",
                                "business_name": "Metrics",
                                "column_description": "List of the metrics in the data list of values like [Drug treatment rate, Final Share, Gross Sales, GTN, Net Sales, New Patients, Patients Start, Price, Regimen Share, SKU Split, Total Patients , Volume]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_2",
                                "business_name": "Segment Name",
                                "column_description": "Segment of the Patients it hold list of values like [1L Non-Squamous PD-L1 High, 1L Non-Squamous PD-L1 Low, 1L Non-Squamous PD-L1 Neg/Unk, 1L Squamous PD-L1 High, 2L CIT Non-Squamous EGFR+, 2L+ CIT Na.ve, Overall] ",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_3",
                                "business_name": "Combination",
                                "column_description": "Class of the product hold list of values like [Combo, Combo + Chemo, Mono, Mono + Chemo, Overall]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_4",
                                "business_name": "Product",
                                "column_description": "Name of the product hold list of values like [Combo, Overall, Product1 IV, Product1 SC]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_5",
                                "business_name": "OVERALL",
                                "column_description": "OVERALL hold list of values like [Combo, IV, Overall, SC]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_6",
                                "business_name": "OVERALL",
                                "column_description": "OVERALL hold values like [Drug tratment rate, Overall]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_7",
                                "business_name": "OVERALL",
                                "column_description": "OVERALL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_8",
                                "business_name": "OVERALL",
                                "column_description": "OVERALL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_9",
                                "business_name": "OVERALL",
                                "column_description": "OVERALL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "type_metric_10",
                                "business_name": "OVERALL",
                                "column_description": "OVERALL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "concatenated",
                                "business_name": "Concatenate Key",
                                "column_description": "Concatenation of all 10 metrics",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_1",
                                "business_name": "Country",
                                "column_description": "List of the countries in the data list of value like [China, France, Germany, Italy, Spain, UK, US]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_2",
                                "business_name": "?",
                                "column_description": "?",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_3",
                                "business_name": "?",
                                "column_description": "?",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_4",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_5",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_6",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_7",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_8",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_9",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "extra_10",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "notes_comments",
                                "business_name": "NULL",
                                "column_description": "NULL",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "year_value",
                                "business_name": "Year Value",
                                "column_description": "Year value for which the output is available",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "data_value",
                                "business_name": "Data Value",
                                "column_description": "Value of metric",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "date_value",
                                "business_name": "Date Value",
                                "column_description": "Date  value for which the output is available",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "forecast_cycle_name",
                                "business_name": "Forecast cycle",
                                "column_description": "Forecast cycle for which the data is submitted for hold list of values like [BP2022, BP2024, BP2025, BP2026, BP2027, MTP2024, MTP2025, MTP2026] ",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "forecast_year",
                                "business_name": "Forecast year",
                                "column_description": "Forecast year for which the data is submitted for",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "therapy_area",
                                "business_name": "Therapy Area",
                                "column_description": "Therapy area details hold value like [Oncology]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "brand_name",
                                "business_name": "Brand",
                                "column_description": "Product name hold list of values like [Product1, Product3, Product4, Product5, Product6, Product7, Product8, Product9]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "indication_name",
                                "business_name": "Indication",
                                "column_description": "Indication details hold list of values like [NSCLC]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "country_name",
                                "business_name": "Country",
                                "column_description": "Country name for which the data is submitted for List of values like[China, France, Germany, Italy, Spain, UK, US]",                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "region_name",
                                "business_name": "Region",
                                "column_description": "Region name for which the data is submitted for hold list of values like [EU5, Global]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "scenario_type_name",
                                "business_name": "Scenario Type",
                                "column_description": "Type of scenario used hold value like [Base, Downside, Upside]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "scenario_name",
                                "business_name": "Scenario",
                                "column_description": "Name of the scenario given by user hold list of values like [Scenario1, Scenario2, Scenario3]",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "description",
                                "business_name": "Description hold list of values like[Competitor impact 1L, Lower IV and SC Price, Updated diagnosed incidence to be double of current values]",
                                "column_description": "Desc",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "submitted_by",
                                "business_name": "Submitted By",
                                "column_description": "Name of user who have submitted/approved the scenario",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                },
                                {
                                "column_name": "submitted_on",
                                "business_name": "Submitted On",
                                "column_description": "Date when the scenario was submitted/approved",
                                "synonyms": "",
                                "data_type": "VARCHAR"
                                }
                            ]
}