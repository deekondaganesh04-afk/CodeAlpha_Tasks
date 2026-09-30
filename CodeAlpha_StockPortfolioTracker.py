# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

# Ask user for stock name and quantity
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in dictionary.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_value = sum(stock_prices[s] * q for s, q in portfolio.items())

print("\nYour Portfolio:")
for s, q in portfolio.items():
    print(f"{s}: {q} shares, Value = ${stock_prices[s] * q}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save = input("Save results to portfolio.txt? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Tracker Results\n")
        for s, q in portfolio.items():
            f.write(f"{s}: {q} shares, Value = ${stock_prices[s] * q}\n")
        f.write(f"\nTotal Investment Value: ${total_value}\n")
    print("Results saved to portfolio.txt")
