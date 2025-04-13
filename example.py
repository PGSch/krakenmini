#!/usr/bin/env python3
from kraken_bot import KrakenBot

def main():
    """Example usage of the Kraken trading bot"""
    try:
        # Create a new bot instance
        bot = KrakenBot()
        
        # Display a simple menu
        print("\nKraken Mini Trading Bot Example")
        print("===============================")
        print("1. Place a limit buy order")
        print("2. Place a limit sell order")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            # Get parameters for limit buy
            ticker = input("Enter ticker (e.g., XBTUSD): ")
            price = input("Enter price: ")
            amount = input("Enter amount: ")
            
            # Confirm the order
            print(f"\nYou are about to place a LIMIT BUY order:")
            print(f"Buy {amount} {ticker.split('USD')[0]} at ${price} USD")
            confirm = input("Confirm? (y/n): ")
            
            if confirm.lower() == 'y':
                result = bot.limit_buy(ticker, price, amount)
                print("\nOrder placed successfully!")
                print(f"Transaction ID: {result.get('result', {}).get('txid', ['Unknown'])[0]}")
            else:
                print("\nOrder cancelled.")
                
        elif choice == '2':
            # Get parameters for limit sell
            ticker = input("Enter ticker (e.g., XBTUSD): ")
            price = input("Enter price: ")
            amount = input("Enter amount: ")
            
            # Confirm the order
            print(f"\nYou are about to place a LIMIT SELL order:")
            print(f"Sell {amount} {ticker.split('USD')[0]} at ${price} USD")
            confirm = input("Confirm? (y/n): ")
            
            if confirm.lower() == 'y':
                result = bot.limit_sell(ticker, price, amount)
                print("\nOrder placed successfully!")
                print(f"Transaction ID: {result.get('result', {}).get('txid', ['Unknown'])[0]}")
            else:
                print("\nOrder cancelled.")
                
        elif choice == '3':
            print("\nExiting program. Goodbye!")
        
        else:
            print("\nInvalid choice. Please run the program again.")
            
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()