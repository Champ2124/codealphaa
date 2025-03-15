# pip install requests
import requests
import time

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity, purchase_price):
        """Add stock to portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
            self.portfolio[symbol]['purchase_price'] = purchase_price
        else:
            self.portfolio[symbol] = {
                'quantity': quantity,
                'purchase_price': purchase_price
            }
        print(f"Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        """Remove stock from portfolio."""
        if symbol in self.portfolio and self.portfolio[symbol]['quantity'] >= quantity:
            self.portfolio[symbol]['quantity'] -= quantity
            if self.portfolio[symbol]['quantity'] == 0:
                del self.portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol} from the portfolio.")
        else:
            print(f"Error: Not enough shares of {symbol} to remove.")

    def get_stock_data(self, symbol):
        """Get real-time stock data using Alpha Vantage API."""
        url = f'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '5min',
            'apikey': self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()

        if 'Time Series (5min)' in data:
            latest_time = list(data['Time Series (5min)'].keys())[0]
            latest_data = data['Time Series (5min)'][latest_time]
            current_price = float(latest_data['4. close'])
            return current_price
        else:
            print(f"Error fetching data for {symbol}. Please check the symbol or try again later.")
            return None

    def calculate_portfolio_value(self):
        """Calculate the current total value of the portfolio."""
        total_value = 0
        for symbol, stock in self.portfolio.items():
            current_price = self.get_stock_data(symbol)
            if current_price is not None:
                total_value += current_price * stock['quantity']
        return total_value

    def calculate_profit_loss(self):
        """Calculate the profit/loss of the portfolio."""
        total_investment = 0
        current_value = 0
        for symbol, stock in self.portfolio.items():
            current_price = self.get_stock_data(symbol)
            if current_price is not None:
                total_investment += stock['purchase_price'] * stock['quantity']
                current_value += current_price * stock['quantity']

        profit_loss = current_value - total_investment
        return profit_loss

    def display_portfolio(self):
        """Display the current portfolio with details."""
        print("\nPortfolio Summary:")
        for symbol, stock in self.portfolio.items():
            current_price = self.get_stock_data(symbol)
            if current_price is not None:
                total_value = current_price * stock['quantity']
                print(f"Stock: {symbol}, Quantity: {stock['quantity']}, Purchase Price: ${stock['purchase_price']}, Current Price: ${current_price:.2f}, Total Value: ${total_value:.2f}")
        print("\nTotal Portfolio Value: ${:.2f}".format(self.calculate_portfolio_value()))
        print(f"Total Profit/Loss: ${self.calculate_profit_loss():.2f}")


def main():
    api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'  # Replace with your own Alpha Vantage API key
    portfolio = StockPortfolio(api_key)

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter the quantity of shares: "))
            purchase_price = float(input("Enter the purchase price per share: $"))
            portfolio.add_stock(symbol, quantity, purchase_price)
        elif choice == '2':
            symbol = input("Enter the stock symbol to remove (e.g., AAPL): ").upper()
            quantity = int(input("Enter the quantity of shares to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            print("Exiting the Stock Portfolio Tracker...")
            break
        else:
            print("Invalid choice. Please try again.")

        # Optional: Add a small delay to prevent too many API calls
        time.sleep(1)


if __name__ == "__main__":
    main()
