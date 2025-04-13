from kraken_bot import KrakenBot

if __name__ == "__main__":
    # Create a bot instance
    bot = KrakenBot()

    # Place a limit buy order (ticker, price, amount)
    # For example, buy 0.01 BTC at $40,000
    bot.limit_buy('XBTUSD', 40000, 0.01)

    # # Place a limit sell order (ticker, price, amount)
    # # For example, sell 0.01 BTC at $45,000
    # bot.limit_sell('XBTUSD', 45000, 0.01)