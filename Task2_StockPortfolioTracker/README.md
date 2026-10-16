# Stock Portfolio Tracker

A simple command-line stock portfolio tracker written in Python, built as part of the CodeAlpha Python Programming internship (Task 2).

## Features
- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN)
- User enters stock symbols and quantities
- Handles invalid symbols and quantities
- Adds up quantities if the same stock is entered more than once
- Shows a formatted summary with the total investment value
- Optionally saves the result to `portfolio.csv`

## Concepts Used
Dictionaries, input/output, basic arithmetic, functions, file handling (`csv`)

## How to Run
Requires Python 3 (no external libraries).

```bash
python portfolio.py
```

## Example
```
=== Stock Portfolio Tracker ===

Available stocks:
  AAPL   $180
  TSLA   $250
  GOOGL  $140
  MSFT   $330
  AMZN   $145

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 10
Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 5
Enter stock symbol (or 'done' to finish): done

----------------------------------------
Stock      Qty     Price         Value
----------------------------------------
AAPL        10       180          1800
TSLA         5       250          1250
----------------------------------------
Total investment:                $3050

Save result to CSV? (y/n): y
Portfolio saved to portfolio.csv
```
