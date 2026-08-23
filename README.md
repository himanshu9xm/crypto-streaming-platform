# crypto-streaming-platform

A. Functional Requirements /b

A.1. Data Ingestion
- Connect to Binance WebSocket API.
- Subscribe to multiple cryptocurrencies.
- Receive live trade events.
- Publish each trade to Pub/Sub.

A.2. Stream Processing
- Read messages from Pub/Sub.
- Validate the schema.
- Filter malformed messages.
- Handle duplicate trade IDs.
- Aggregate data at different intervals.
- Compute metrics like:
  - Average price
  - High
  - Low
  - Volume
  - Trade count
 
A.3. Storage
- Store:
  - Raw trades
  - 1-second aggregates
  - 1-minute aggregates
  - 5-minute aggregates
  - Hourly aggregates
  - Daily aggregates
 
A.4. Dashboard
- Allow users to:
  - View live prices.
  - Select a cryptocurrency.
  - Switch between:
    - Last minute
    - Last hour
    - Last day
    - Last week
  - View charts and summary metrics.
