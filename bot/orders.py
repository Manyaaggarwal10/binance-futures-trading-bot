import logging

logger = logging.getLogger(__name__)

def place_order(client, symbol, side, order_type, qty, price=None):


    logger.info(
        f"Placing order: {side} {order_type} {symbol} qty={qty} price={price}"
    )

    if order_type == "MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=qty
        )

    else:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=qty,
            price=price,
            timeInForce="GTC"
        )

    logger.info(f"Order response: {order}")
    return order

