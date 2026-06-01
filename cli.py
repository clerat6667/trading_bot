import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("SECRET_KEY")
def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Example: BTCUSDT"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"]
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"]
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(args.side)

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        price = validate_price(
            args.price
        )

        if (
            order_type == "LIMIT"
            and price is None
        ):
            raise ValueError(
                "LIMIT order requires --price"
            )

        print("\nORDER REQUEST")
        print("-" * 40)

        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if price:
            print(f"Price    : {price}")

        client = BinanceClient(
            API_KEY,
            API_SECRET
        )

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\nORDER RESPONSE")
        print("-" * 40)

        print(
            f"Order ID      : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status        : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty  : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Average Price : "
            f"{response.get('avgPrice')}"
        )

        print("\nSUCCESS")

    except Exception as e:

        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()
