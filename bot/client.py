from binance.client import Client
from dotenv import load_dotenv
import os
import logging

# Load variables from .env file

load_dotenv()

# Read API credentials

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

# Basic validation

if not API_KEY or not API_SECRET:
    raise ValueError("Missing API credentials. Check your .env file.")

# Configure logger

logger = logging.getLogger(__name__)

def get_client():

    try:
        client = Client(API_KEY, API_SECRET)


        # Binance USDT-M Futures Testnet base URL
        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet client initialized successfully.")
        return client

    except Exception as e:
        logger.error(f"Failed to initialize Binance client: {str(e)}")
        raise

