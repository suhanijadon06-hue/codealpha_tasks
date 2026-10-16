STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
}


def main():
    portfolio = {}

    while True:
        name = input("Enter stock symbol (or 'done' to finish): ").upper()
        if name == "DONE":
            break
        qty = int(input(f"Enter quantity of {name}: "))
        portfolio[name] = portfolio.get(name, 0) + qty

    total = 0
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        total += value
        print(f"{name}: {qty} x ${STOCK_PRICES[name]} = ${value}")

    print(f"Total investment: ${total}")


if __name__ == "__main__":
    main()
