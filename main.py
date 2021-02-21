# This program is designed by Albert Jokelin.
# This program analyses NASDAQ Companies and makes a highly profitable portfolio. If you want NSE, add those symbols to the Symbols list in scrapper.py
# This project has been built for educational purposes, DO NOT use this to make your portfolio choices
# If you use this software, any liability it brings will solely be your responisibiliy.
# Import required libraries
import pandas as pd
import numpy as np
import requests
import csv
import yfinance as yf
import datetime
import time
import io

# To optimize the portfolio
import cvxpy as cp
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import EfficientFrontier
from pypfopt import objective_functions
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

 
# Get the names of the companies
def get_name(ticker):
    url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query='+ticker+'&region=1&lang=en'
    result = requests.get(url).json()
    for r in result['ResultSet']['Result']:
        if r['symbol'] == ticker:
            return r['name']

if __name__=="__main__":
    try:
        df = pd.read_csv('scrapper.csv')
    except Exception:
        print("CSV file not found")


    assets = df.columns

    # Calculate the annual returns 
    mu  = expected_returns.mean_historical_return(df) # Mean
    S = risk_models.sample_cov(df) # Sample Covariance matrix


    # Optimize for the maximal Sharpe Ratio
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()

    cleaned_weights = ef.clean_weights()

    # Get the discrete allocation of each share per stock
    portfolio_val = 5000 # How much money you want to invest in USD
    latest_prices = get_latest_prices(df)
    weights = cleaned_weights
    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=portfolio_val)
    allocation, leftover = da.lp_portfolio() # Allocation in var-1 and leftover amount in var-2

    # Store all company names in a list
    company_name = []
    discrete_allocation_list = []
    for symbol in allocation:
        company_name.append(get_name(symbol))
        discrete_allocation_list.append(allocation.get(symbol))

    # Create a dataframe for the portfolio
    portfolio_df = pd.DataFrame(columns=['Company_name', 'Company_Ticker', 'Discrete_Val_'+str(portfolio_val)])

    portfolio_df['Company_name'] = company_name
    portfolio_df['Company_Ticker'] = allocation
    portfolio_df['Discrete_Val_'+str(portfolio_val)] = discrete_allocation_list

    # Display the portfolio
    print(portfolio_df)
    #print("\nDiscrete Allocation: ", allocation)
    print("\nFunds remaining: $", leftover)
    #print(cleaned_weights)
    ef.portfolio_performance(verbose=False)