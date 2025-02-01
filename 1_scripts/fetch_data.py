import os
import requests
import pandas as pd
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Logging configuration
logging.basicConfig(
    filename="5_logs/fetch_data.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# CoinGecko API endpoint
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
CRYPTOCURRENCIES = ["bitcoin", "ethereum", "binancecoin"]
PARAMS = {"ids": ",".join(CRYPTOCURRENCIES), "vs_currencies": "usd"}

def fetch_crypto_prices():
    """Fetch cryptocurrency prices from CoinGecko API and save to CSV."""
    try:
        response = requests.get(COINGECKO_API_URL, params=PARAMS)
        response.raise_for_status()
        data = response.json()

        # Convert to DataFrame
        records = []
        for crypto in CRYPTOCURRENCIES:
            records.append({
                "timestamp": pd.Timestamp.now(),
                "crypto": crypto,
                "price_usd": data[crypto]["usd"]
            })

        df = pd.DataFrame(records)

        # Save data
        file_path = "2_data/crypto_prices.csv"
        df.to_csv(file_path, mode="a", index=False, header=not os.path.exists(file_path))

        logging.info("Successfully fetched and saved crypto price data.")

    except Exception as e:
        logging.error(f"Error fetching crypto prices: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_crypto_prices()