import os
import logging
from google.cloud import bigquery

# Logging configuration
LOG_FILE = "5_logs/test_connection.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def test_bigquery_connection():
    """Test BigQuery connection by listing datasets."""
    try:
        # Convert UNIX path to Windows if needed
        key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

        if not key_path:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set.")
        
        if key_path.startswith("/mnt/"):
            key_path = key_path.replace("/mnt/c/", "C:/").replace("/", "\\")
        
        if not os.path.exists(key_path):
            raise FileNotFoundError(f"Service account key file not found: {key_path}")

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
        logging.info("Using service account key: %s", key_path)

        # Initialize BigQuery client
        client = bigquery.Client()

        # List datasets in the project
        datasets = list(client.list_datasets())

        if datasets:
            logging.info("BigQuery connection successful. Available datasets:")
            print("BigQuery connection successful. Available datasets:")
            for dataset in datasets:
                dataset_id = dataset.dataset_id
                logging.info(f"- {dataset_id}")
                print(f"- {dataset_id}")
        else:
            logging.warning("BigQuery connection successful, but no datasets found.")
            print("BigQuery connection successful, but no datasets found.")

    except Exception as e:
        logging.error(f"BigQuery connection failed: {e}")
        print(f"BigQuery connection failed: {e}")

if __name__ == "__main__":
    test_bigquery_connection()