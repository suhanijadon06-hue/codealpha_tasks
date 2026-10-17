import csv
import os
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "NVDA": 120,
    "META": 500,
    "NFLX": 650,
}

CSV_FILE = "portfolio.csv"
TXT_FILE = "portfolio_report.txt"


class Portfolio:
    def __init__(self):
        # symbol -> {"qty": int, "cost": float (total amount paid)}
        self.holdings = {}

    def buy(self, symbol, qty, price):
        holding = self.holdings.setdefault(symbol, {"qty": 0, "cost": 0.0})
        holding["qty"] += qty
        holding["cost"] += qty * price

    def sell(self, symbol, qty):
        holding = self.holdings[symbol]
        avg_price = holding["cost"] / holding["qty"]
        holding["qty"] -= qty
        holding["cost"] -= avg_price * qty
        if holding["qty"] == 0:
            del self.holdings[symbol]
        return (STOCK_PRICES[symbol] - avg_price) * qty

    def rows(self):
        """Return one row per holding plus the portfolio totals."""
        rows = []
        for symbol, h in sorted(self.holdings.items()):
            value = h["qty"] * STOCK_PRICES[symbol]
            rows.append({
                "symbol": symbol,
                "qty": h["qty"],
                "avg": h["cost"] / h["qty"],
                "price": STOCK_PRICES[symbol],
                "cost": h["cost"],
                "value": value,
                "pl": value - h["cost"],
            })
        total_cost = sum(r["cost"] for r in rows)
        total_value = sum(r["value"] for r in rows)
        return rows, total_cost, total_value

    def save_csv(self, filename=CSV_FILE):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "TotalCost"])
            for symbol, h in sorted(self.holdings.items()):
                writer.writerow([symbol, h["qty"], round(h["cost"], 2)])

    def load_csv(self, filename=CSV_FILE):
        self.holdings = {}
        with open(filename, newline="") as f:
            for row in csv.DictReader(f):
                if row["Symbol"] not in STOCK_PRICES:
                    continue
                self.holdings[row["Symbol"]] = {
                    "qty": int(row["Quantity"]),
                    "cost": float(row["TotalCost"]),
                }

    def save_report(self, filename=TXT_FILE):
        rows, total_cost, total_value = self.rows()
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO REPORT\n")
            f.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M}\n\n")
            f.write(format_table(rows, total_cost, total_value))


def format_table(rows, total_cost, total_value):
    line = "-" * 78
    out = [line,
           f"{'Stock':<7}{'Qty':>6}{'Avg Buy':>10}{'Price':>9}"
           f"{'Invested':>12}{'Value':>12}{'P/L':>12}{'Alloc':>10}",
           line]
    for r in rows:
        alloc = r["value"] / total_value * 100 if total_value else 0
        out.append(f"{r['symbol']:<7}{r['qty']:>6}{r['avg']:>10.2f}{r['price']:>9}"
                   f"{r['cost']:>12.2f}{r['value']:>12.2f}{r['pl']:>+12.2f}{alloc:>9.1f}%")
    out.append(line)
    pl = total_value - total_cost
    pct = pl / total_cost * 100 if total_cost else 0
    out.append(f"Total invested: ${total_cost:,.2f}")
    out.append(f"Current value:  ${total_value:,.2f}")
    out.append(f"Profit/Loss:    ${pl:+,.2f} ({pct:+.2f}%)")
    return "\n".join(out) + "\n"


def ask_symbol(valid):
    symbol = input("Stock symbol: ").strip().upper()
    if symbol not in valid:
        print("Invalid symbol.")
        return None
    return symbol


def ask_int(prompt, maximum=None):
    text = input(prompt).strip()
    if not text.isdigit() or int(text) == 0:
        print("Please enter a positive whole number.")
        return None
    if maximum is not None and int(text) > maximum:
        print(f"You only have {maximum} shares.")
        return None
    return int(text)


def ask_price(default):
    text = input(f"Buy price per share (Enter for current ${default}): ").strip()
    if not text:
        return default
    try:
        price = float(text)
    except ValueError:
        price = 0
    if price <= 0:
        print("Invalid price, using current price.")
        return default
    return price


def show_market():
    print("\nCurrent market prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price}")


def menu():
    print("""
=== Stock Portfolio Tracker ===
1. View market prices
2. Buy stock
3. Sell stock
4. View portfolio
5. Save portfolio (CSV + TXT report)
6. Load portfolio from CSV
7. Exit""")
    return input("Choose an option: ").strip()


def main():
    portfolio = Portfolio()

    while True:
        choice = menu()

        if choice == "1":
            show_market()

        elif choice == "2":
            symbol = ask_symbol(STOCK_PRICES)
            if symbol:
                qty = ask_int(f"Quantity of {symbol}: ")
                if qty:
                    price = ask_price(STOCK_PRICES[symbol])
                    portfolio.buy(symbol, qty, price)
                    print(f"Bought {qty} {symbol} at ${price:.2f}.")

        elif choice == "3":
            if not portfolio.holdings:
                print("Your portfolio is empty.")
                continue
            symbol = ask_symbol(portfolio.holdings)
            if symbol:
                qty = ask_int("Quantity to sell: ", portfolio.holdings[symbol]["qty"])
                if qty:
                    pl = portfolio.sell(symbol, qty)
                    print(f"Sold {qty} {symbol} at ${STOCK_PRICES[symbol]}. "
                          f"Realised P/L: ${pl:+.2f}")

        elif choice == "4":
            if not portfolio.holdings:
                print("Your portfolio is empty.")
            else:
                print()
                print(format_table(*portfolio.rows()))

        elif choice == "5":
            if not portfolio.holdings:
                print("Nothing to save.")
            else:
                portfolio.save_csv()
                portfolio.save_report()
                print(f"Saved to {CSV_FILE} and {TXT_FILE}.")

        elif choice == "6":
            if os.path.exists(CSV_FILE):
                portfolio.load_csv()
                print(f"Loaded {len(portfolio.holdings)} holding(s) from {CSV_FILE}.")
            else:
                print(f"{CSV_FILE} not found.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
