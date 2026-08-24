import asyncio
import json
import logging

import websockets

from datetime import datetime, timezone

from config import Config
from models import TradeEvent
from pubsub_publisher import PubSubPublisher


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def build_stream_url() -> str:
    streams = "/".join(
        f"{symbol}@trade"
        for symbol in Config.SYMBOLS
    )

    return f"{Config.BINANCE_WS_URL}/stream?streams={streams}"

publisher = PubSubPublisher(
        project_id=Config.GCP_PROJECT_ID,
        topic_id=Config.PUBSUB_TOPIC_ID,
    )

async def consume_trades():
    url = build_stream_url()
    

    while True:
        try:
            logger.info(
                "Connecting to Binance for symbols: %s",
                Config.SYMBOLS,
            )

            async with websockets.connect(url) as websocket:
                logger.info("Connected to Binance")

                async for message in websocket:
                    payload = json.loads(message)
                    trade = payload["data"]

                    trade_event = TradeEvent(
                        exchange="binance",
                        symbol=trade["s"],
                        trade_id=trade["t"],
                        price=float(trade["p"]),
                        quantity=float(trade["q"]),
                        event_time=datetime.fromtimestamp(
                            trade["E"] / 1000,
                            tz=timezone.utc,
                        ),
                    )

                    message_id = publisher.publish(
                        trade_event.to_json()
                    )

                    logger.info(
                        "Published trade: symbol=%s trade_id=%s message_id=%s",
                        trade_event.symbol,
                        trade_event.trade_id,
                        message_id,
                    )

        except Exception as exc:
            logger.error(
                "WebSocket connection failed: %s",
                exc,
            )

            logger.info(
                "Reconnecting in %s seconds...",
                Config.RECONNECT_DELAY_SECONDS,
            )

            await asyncio.sleep(
                Config.RECONNECT_DELAY_SECONDS
            )


if __name__ == "__main__":
    asyncio.run(consume_trades())