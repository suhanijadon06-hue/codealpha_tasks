import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
}


def show_prices():
    print("\nAvailable stocks:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name:<6} ${price}")
    print()


def get_portfolio():
    portfolio = {}
    while True:
        name = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Unknown stock symbol. Please choose from the list above.")
            continue

        qty = input(f"Enter quantity of {name}: ").strip()
        if not qty.isdigit() or int(qty) == 0:
            print("Quantity must be a positive whole number.")
            continue

        portfolio[name] = portfolio.get(name, 0) + int(qty)
    return portfolio


def build_rows(portfolio):
    rows = []
    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        rows.append([name, qty, price, qty * price])
    return rows


def print_summary(rows, total):
    print("\n" + "-" * 40)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * 40)
    for name, qty, price, value in rows:
        print(f"{name:<8}{qty:>6}{price:>10}{value:>14}")
    print("-" * 40)
    print(f"{'Total investment:':<24}{'$' + str(total):>14}")


def save_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
        writer.writerow(["Saved on", datetime.now().strftime("%Y-%m-%d %H:%M")])
    print(f"Portfolio saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_prices()
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered.")
        return

    rows = build_rows(portfolio)
    total = sum(row[3] for row in rows)
    print_summary(rows, total)

    if input("\nSave result to CSV? (y/n): ").strip().lower() == "y":
        save_csv(rows, total)


if __name__ == "__main__":
    main()
