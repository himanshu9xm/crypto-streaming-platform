from dataclasses import dataclass
from datetime import datetime, timezone
import json


@dataclass
class TradeEvent:
    exchange: str
    symbol: str
    trade_id: int
    price: float
    quantity: float
    event_time: datetime

    def to_json(self) -> bytes:
        payload = {
            "exchange": self.exchange,
            "symbol": self.symbol,
            "trade_id": self.trade_id,
            "price": self.price,
            "quantity": self.quantity,
            "event_time": self.event_time.astimezone(
                timezone.utc
            ).isoformat(),
        }

        return json.dumps(payload).encode("utf-8")