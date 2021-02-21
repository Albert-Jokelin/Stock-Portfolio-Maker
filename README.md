# Stock portfolio maker 

## What is it?
It is a python program that creates a stock portfolio based on the historical data of the companies listed in the NASDAQ index. 

Libraries used:
*  Numpy
* Pandas
* PyPortfolioOpt
* Yahoo finance API (yfinance)

## How do I use it?

1. Clone the repository in to your machine
2. Install all the required dependencies in requirements.txt
3. Run scrapper.py
4. ```scrapper.csv``` is stored in your root directory, move it to ```/Stock_portfolio-Maker/``` folder.
5. Open ```scrapper.csv``` and erase the first row. It says "Adj. Close".
6. Run main.py.

## Changing the parameters passed:
1. Changing the ticker symbol used to determine the portfolio
    * Open scrapper.py and change the values in ```Symbols```
2. Changing the portfolio value:
    * Open main.py and change the value of ```portfolio_val```. It is set at $5000 by default.
