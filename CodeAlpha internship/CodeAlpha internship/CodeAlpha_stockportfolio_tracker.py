"""
Stock Portfolio Tracker
A simple program to calculate total investment value based on stock holdings
"""

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 175,
    "META": 350,
    "NVDA": 500
}

def get_portfolio():
    """Get stock holdings from user input"""
    portfolio = {}
    
    print("=" * 50)
    print("Stock Portfolio Tracker")
    print("=" * 50)
    print("\nAvailable stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")
    print()
    
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").upper().strip()
        
        if stock_name == "DONE":
            if not portfolio:
                print("Please enter at least one stock!")
                continue
            break
        
        if stock_name not in stock_prices:
            print(f"Error: '{stock_name}' not found in available stocks. Try again.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity <= 0:
                print("Please enter a positive number!")
                continue
            
            if stock_name in portfolio:
                portfolio[stock_name] += quantity
                print(f"Updated {stock_name} quantity to {portfolio[stock_name]}")
            else:
                portfolio[stock_name] = quantity
                print(f"Added {stock_name} x {quantity} to portfolio")
            print()
        
        except ValueError:
            print("Please enter a valid number!")
    
    return portfolio

def calculate_total_investment(portfolio):
    """Calculate total investment value"""
    total = 0
    print("\n" + "=" * 50)
    print("Portfolio Summary")
    print("=" * 50)
    
    for stock, quantity in portfolio.items():
        stock_value = stock_prices[stock] * quantity
        total += stock_value
        print(f"{stock:8} | Qty: {quantity:4} | Price: ${stock_prices[stock]:6.2f} | Total: ${stock_value:10.2f}")
    
    print("-" * 50)
    print(f"{'TOTAL INVESTMENT VALUE':30} ${total:10.2f}")
    print("=" * 50)
    
    return total

def save_to_file(portfolio, total, filename="portfolio_results.txt"):
    """Save portfolio results to a file"""
    try:
        with open(filename, 'w') as file:
            file.write("=" * 50 + "\n")
            file.write("Stock Portfolio Tracker - Results\n")
            file.write("=" * 50 + "\n\n")
            
            for stock, quantity in portfolio.items():
                stock_value = stock_prices[stock] * quantity
                file.write(f"{stock:8} | Qty: {quantity:4} | Price: ${stock_prices[stock]:6.2f} | Total: ${stock_value:10.2f}\n")
            
            file.write("-" * 50 + "\n")
            file.write(f"TOTAL INVESTMENT VALUE: ${total:10.2f}\n")
            file.write("=" * 50 + "\n")
        
        print(f"\nResults saved to '{filename}'")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    """Main program execution"""
    portfolio = get_portfolio()
    total = calculate_total_investment(portfolio)
    
    # Ask user if they want to save results
    save_choice = input("\nWould you like to save results to a file? (yes/no): ").lower().strip()
    if save_choice in ['yes', 'y']:
        save_to_file(portfolio, total)
    
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
