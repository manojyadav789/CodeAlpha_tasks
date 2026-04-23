# Stock Portfolio Tracker

A simple Python program to track and manage your stock portfolio, calculate total investment value, and analyze your holdings.

## About

This Stock Portfolio Tracker helps you manage your investment portfolio by:
- Adding and tracking multiple stock holdings
- Calculating the total value of your portfolio
- Providing individual stock performance metrics
- Supporting real-time or predefined stock prices

## Features

- **Multiple Stock Support**: Track holdings in 7 major stocks (AAPL, TSLA, GOOGL, MSFT, AMZN, META, NVDA)
- **Real-time Calculations**: Instantly calculate portfolio value and individual stock metrics
- **User-friendly Interface**: Simple command-line interface for easy navigation
- **Price Tracking**: Built-in stock prices with easy updates
- **Portfolio Analysis**: View total investment, current value, and performance

## Requirements

- Python 3.x

## Running the Application

```bash
python stock_portfolio_tracker.py
```

## How to Use

1. Run the program with Python
2. The program displays available stocks and their prices
3. Enter stock names and quantities when prompted
4. Type 'done' to finish adding stocks
5. View your portfolio summary with total value and cost basis
6. Track individual stock performance and allocation

## Supported Stocks

- **AAPL** - Apple: $180
- **TSLA** - Tesla: $250
- **GOOGL** - Google: $140
- **MSFT** - Microsoft: $380
- **AMZN** - Amazon: $175
- **META** - Meta: $350
- **NVDA** - NVIDIA: $500

## Features Overview

- Add stocks to your portfolio
- Automatically calculate total investment cost
- Calculate current portfolio value
- View individual stock metrics
- User input validation and error handling

## Example Usage

```
==================================================
Stock Portfolio Tracker
==================================================

Available stocks and prices:
  AAPL: $180
  TSLA: $250
  GOOGL: $140
  ...

Enter stock name (or 'done' to finish): AAPL
Enter quantity of AAPL: 10
```

## Author

Developed as part of CodeAipha Internship Task 1
you have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Guess a letter: e
Correct!

Word: _ e _ _ _ _
Guess a letter: a
Wrong! Incorrect guesses left: 5
```

## Features

- Input validation (only accepts single alphabetic letters)
- Prevents duplicate guesses
- Real-time feedback on correct/incorrect guesses
- Displays remaining incorrect guesses
- Shows the final word upon game completion
