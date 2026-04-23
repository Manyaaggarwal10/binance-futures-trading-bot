def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")

def validate_price(order_type, price):
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Valid price required for LIMIT order")
