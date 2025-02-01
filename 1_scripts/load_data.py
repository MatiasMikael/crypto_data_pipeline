import os
import logging
import pandas as pd
from google.cloud import bigquery

# Logging configuration
LOG_FILE = "5_logs/load_data.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# BigQuery settings
PROJECT_ID = "crypto-data-pipeline-449309"
DATASET_ID = "crypto_dataset"
TABLE_ID = "crypto_prices"
DATA_FILE = "2_data/crypto_prices.csv"

def load_data_to_bigquery():
    """Load cryptocurrency price data from CSV to BigQuery."""
    try:
        # Ensure the environment variable is set correctly
        key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if not key_path:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set.")

        # Initialize BigQuery client
        client = bigquery.Client()

        # Check if CSV file exists
        if not os.path.exists(DATA_FILE):
            raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

        # Read CSV file
        df = pd.read_csv(DATA_FILE)

        # Convert timestamp column to datetime format
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Define table reference
        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

        # Configure job
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND"  # Append data instead of overwriting
        )

        # Load data into BigQuery
        job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()  # Wait for the job to complete

        logging.info("Successfully loaded %d rows into BigQuery table: %s", len(df), table_ref)
        print(f"Successfully loaded {len(df)} rows into BigQuery table: {table_ref}")

    except Exception as e:
        logging.error(f"Error loading data to BigQuery: {e}")
        print(f"Error loading data to BigQuery: {e}")

if __name__ == "__main__":
    load_data_to_bigquery()