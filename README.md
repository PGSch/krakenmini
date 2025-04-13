# Kraken Mini Trading Bot

![Trading Bot Status](https://img.shields.io/badge/status-active-green)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

A lightweight and straightforward trading bot for the Kraken cryptocurrency exchange that provides simple limit order functionality.

## Features

- **Limit Buy Orders**: Place limit buy orders for cryptocurrencies
- **Limit Sell Orders**: Place limit sell orders for cryptocurrencies
- **Secure Authentication**: Uses Kraken's API authentication mechanism
- **Simple Interface**: Easy-to-use functions for trading operations

## Prerequisites

- Python 3.6 or higher
- A Kraken account with API keys
- Basic understanding of cryptocurrency trading

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/krakenmini.git
   cd krakenmini
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # On Windows
   .\.venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API credentials:
   - Copy `.env.example` to `.env`
   - Add your Kraken API key and secret to the `.env` file

## Configuration

Create a `.env` file in the root directory with the following content:

```
KRAKEN_API_KEY=your_api_key_here
KRAKEN_API_SECRET=your_api_secret_here
```

Replace `your_api_key_here` and `your_api_secret_here` with your actual Kraken API credentials.

## Usage

### Basic Usage

Import the `KrakenBot` class and create an instance:

```python
from kraken_bot import KrakenBot

# Initialize the bot
bot = KrakenBot()
```

### Placing Limit Buy Orders

```python
# Parameters: ticker, price, amount
result = bot.limit_buy('XBTUSD', 40000, 0.01)
print(result)
```

### Placing Limit Sell Orders

```python
# Parameters: ticker, price, amount
result = bot.limit_sell('XBTUSD', 45000, 0.01)
print(result)
```

### Example Script

You can use the provided example script to interact with the bot through a simple menu:

```bash
python example.py
```

This will guide you through placing limit orders with a step-by-step interface.

### Common Kraken Ticker Symbols

- XBTUSD - Bitcoin/USD
- ETHUSD - Ethereum/USD
- XLTCZUSD - Litecoin/USD
- XXRPZUSD - Ripple/USD
- DOTUSD - Polkadot/USD

## Response Format

Successful API responses are returned as Python dictionaries with the following structure:

```python
{
    'error': [],
    'result': {
        'txid': ['OE4MQV-4KRYL-KKMHPF'],  # Transaction ID(s)
        'descr': {
            'order': 'buy 0.01000000 XBTUSD @ limit 40000'
        }
    }
}
```

## Error Handling

The bot will raise exceptions with helpful error messages if:
- API credentials are missing or invalid
- The API request fails
- The API returns an error response

## Project Structure

- `kraken_bot.py` - Main bot implementation with trading functions
- `main.py` - Simple script to demonstrate basic usage
- `example.py` - Interactive example with a user-friendly menu
- `requirements.txt` - Required Python packages
- `.env.example` - Template for API credentials

## Security Considerations

- Never share your API keys or include them in version control
- Consider restricting your API keys to only the necessary permissions
- Use small amounts for testing before executing larger trades

## Limitations

- This is a minimalist implementation focused on limit orders only
- Advanced trading features (stop-loss, trailing stops, etc.) are not implemented
- No automatic trading strategies or technical analysis tools are included

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms included in the LICENSE file.

## Disclaimer

Trading cryptocurrencies involves significant risk. This tool is provided for educational purposes only. Use at your own risk. The authors are not responsible for any financial losses incurred while using this software.