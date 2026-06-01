# Binance Futures Testnet Trading Bot

A simple Python trading bot that places
MARKET and LIMIT orders on Binance
Futures Testnet.

## Installation

```bash
pip install -r requirements.txt
```

## Configure API Keys

Open:

bot/cli.py

Replace:

```python
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
```

with your Binance Futures Testnet keys.

## MARKET Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

## LIMIT Order

```bash
python -m bot.cli \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 120000
```

## Features

- MARKET Orders
- LIMIT Orders
- BUY / SELL
- Input Validation
- Logging
- Exception Handling
- Modular Design

## Log File

Generated automatically:

```text
trading_bot.log
```
