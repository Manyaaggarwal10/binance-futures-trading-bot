# Binance Futures Testnet Trading Bot

A simple and user-friendly Python trading bot built for Binance Futures Testnet (USDT-M).
This project was created as part of a Python Developer application task.

It allows users to place **MARKET** and **LIMIT** orders using either:

* Command Line Interface (CLI)
* Lightweight Web UI using Streamlit

The project focuses on clean code structure, reusable modules, input validation, logging, and proper error handling.

---

# Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL sides
* Binance Futures Testnet integration
* Input validation with clear error messages
* Logs API requests, responses, and errors
* CLI mode using argparse
* Web UI mode using Streamlit
* Modular project structure

---

# Project Structure

```text
trading_bot/
│── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│── cli.py
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

# Tech Stack

* Python 3.x
* python-binance
* Streamlit
* argparse
* python-dotenv
* logging

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Add API Keys

Create a `.env` file in root folder:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
```

---

# Run the CLI Version

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 150000
```

---

# Run the Web UI Version

```bash
streamlit run app.py
```

This opens a simple browser interface where users can:

* Select symbol
* Choose BUY / SELL
* Choose MARKET / LIMIT
* Enter quantity
* Enter price (for LIMIT orders only)
* Place order with one click

---

# Logging

All API requests, responses, and errors are stored in:

```text
logs/app.log
```

---

# Assumptions

* Binance Futures Testnet account is active
* Valid API keys are available
* User has sufficient testnet balance
* Supported symbols are common USDT pairs such as BTCUSDT, ETHUSDT, BNBUSDT

---

# Notes

This project is intended for testnet/demo trading only.
No real funds are used.

---

# Author

Built by Manya Aggarwal as part of a Python Developer application task.
