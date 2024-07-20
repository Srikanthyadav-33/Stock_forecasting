# Stock Forecasting

This project fetches, visualizes, and forecasts stock data using the Alpha Vantage API.

## Setup

1. Clone the repository.
2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. Set your Alpha Vantage API key as an environment variable:
    ```sh
    export ALPHAVANTAGE_API_KEY=your_api_key  # On Windows use `set ALPHAVANTAGE_API_KEY=your_api_key`
    ```

## Usage

1. Fetch stock data:
    ```sh
    python fetch_data.py
    ```
2. Visualize stock data:
    ```sh
    python visualize_data.py
    ```
3. Forecast stock prices:
    ```sh
    python forecast.py
    ```
