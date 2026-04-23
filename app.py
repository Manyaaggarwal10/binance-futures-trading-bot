import streamlit as st
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
validate_symbol,
validate_side,
validate_order_type,
validate_quantity,
validate_price
)



# Page Config


st.set_page_config(
page_title="Binance Futures Testnet Bot",
page_icon="📈",
layout="centered"
)



# Custom Styling


st.markdown("""

<style>
.main-title {
    font-size: 34px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 20px;
}
.sub-text {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #f4f4f4;
}
</style>

""", unsafe_allow_html=True)


# Header


st.markdown('<div class="main-title">📈 Binance Futures Testnet Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Place MARKET or LIMIT orders using Binance Futures Testnet</div>', unsafe_allow_html=True)



# Form UI

with st.form("trade_form"):


    symbol = st.selectbox(
        "Symbol",
        ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    )

    side = st.radio(
        "Side",
        ["BUY", "SELL"],
        horizontal=True
    )

    order_type = st.selectbox(
        "Order Type",
        ["MARKET", "LIMIT"]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0.0,
        value=0.001,
        step=0.001,
        format="%.6f"
    )

    price = None

    if order_type == "LIMIT":
        price = st.number_input(
            "Price",
            min_value=0.0,
            value=100000.0,
            step=100.0
        )

    submit = st.form_submit_button("🚀 Place Order")




# On Submit

if submit:


    try:
        # Validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        # Connect Client
        client = get_client()

        # Place Order
        order = place_order(
            client=client,
            symbol=symbol,
            side=side,
            order_type=order_type,
            qty=quantity,
            price=price
        )

        # Success
        st.success("Order placed successfully!")

        st.markdown("### Order Response")

        st.info(f"""

                Order ID: {order["orderId"]}

                Status: {order["status"]}

                Executed Qty: {order["executedQty"]}

                Avg Price: {order.get("avgPrice", "N/A")}
                """)


    except Exception as e:
        st.error(f" {str(e)}")

