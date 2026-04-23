import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
validate_symbol,
validate_side,
validate_order_type,
validate_quantity,
validate_price
)
from bot.logging_config import logging

def main():
    parser = argparse.ArgumentParser(description="Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.qty)
        validate_price(args.type, args.price)

        client = get_client()

        print("----- ORDER REQUEST -----")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.qty}")

        if args.price:
            print(f"Price    : {args.price}")

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price
        )

        print("\n----- ORDER RESPONSE -----")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Qty:", order["executedQty"])

        if "avgPrice" in order:
            print("Avg Price:", order["avgPrice"])

        print("\nOrder placed successfully!")

    except Exception as e:
        logging.error(str(e))
        print("\nError:", str(e))


if __name__ == "__main__":
    main()
