# Stock Portfolio Tracker

A menu-driven command-line stock portfolio tracker written in Python, built as part of the CodeAlpha Python Programming internship (Task 2).

## Features
- Hardcoded dictionary of current stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN, NVDA, META, NFLX)
- **Buy stocks** with a custom buy price (or use the current market price)
- **Sell stocks** and see the realised profit/loss
- **Average buy price** is tracked when you buy the same stock more than once
- **Portfolio summary** with invested amount, current value, profit/loss and allocation % for each stock
- **Save** the portfolio to `portfolio.csv` and a readable report to `portfolio_report.txt`
- **Load** a saved portfolio back from CSV
- Validates every input (symbols, quantities, prices, menu options)

## Concepts Used
Dictionaries, classes (OOP), functions, loops, input/output, arithmetic, string formatting, file handling (`csv`, `os`)

## How to Run
Requires Python 3 (no external libraries).

```bash
python portfolio.py
```

## Menu
```
=== Stock Portfolio Tracker ===
1. View market prices
2. Buy stock
3. Sell stock
4. View portfolio
5. Save portfolio (CSV + TXT report)
6. Load portfolio from CSV
7. Exit
```

## Example Output
```
------------------------------------------------------------------------------
Stock     Qty   Avg Buy    Price    Invested       Value         P/L     Alloc
------------------------------------------------------------------------------
AAPL        6    150.00      180      900.00     1080.00     +180.00     51.9%
TSLA        4    250.00      250     1000.00     1000.00       +0.00     48.1%
------------------------------------------------------------------------------
Total invested: $1,900.00
Current value:  $2,080.00
Profit/Loss:    $+180.00 (+9.47%)
```
