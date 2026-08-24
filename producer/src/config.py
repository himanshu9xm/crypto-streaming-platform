import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    BINANCE_WS_URL = os.getenv(
        "BINANCE_WS_URL",
        "wss://stream.binance.com:9443",
    )

    SYMBOLS = [
        symbol.strip().lower()
        for symbol in os.getenv(
            "SYMBOLS",
            "btcusdt",
        ).split(",")
        if symbol.strip()
    ]

    RECONNECT_DELAY_SECONDS = int(
        os.getenv("RECONNECT_DELAY_SECONDS", "5")
    )

    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")

    PUBSUB_TOPIC_ID = os.getenv(
        "PUBSUB_TOPIC_ID",
        "crypto-trades",
    )