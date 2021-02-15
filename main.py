# This program is designed by Albert Jokelin.
# This program analyses NASDAQ Companies and makes a highly profitable portfolio
# The code for the scrapper was taken from https://towardsdatascience.com/downloading-historical-stock-prices-in-python-93f85f059c1f
# This project has been built for educational purposes, DO NOT use this to make your portfolio choices
# If you use this software, any liability it brings will solely be your responisibiliy

# Import required libraries
import pandas as pd
import numpy as np
import requests
import csv
import yfinance as yf
import datetime
import time
import io
# ---- WEB SCRAPER BEGIN -----
# Set date
start = datetime.datetime(2020,2,1)
end = datetime.datetime(2020,10,11)

#Load and store the data
url="https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
s = requests.get(url).content
nasdaq_list = pd.read_csv(io.StringIO(s.decode('utf-8')))
Symbols = nasdaq_list['Symbol'].tolist()

# create empty dataframe
stock_final = pd.DataFrame()
# iterate over each symbol
for i in Symbols:  
    
    # print the symbol which is being downloaded
    print( str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)  
    
    try:
        # download the stock price 
        stock = []
        stock = yf.download(i,start=start, end=end, progress=False)
        
        # append the individual stock prices 
        if len(stock) == 0:
            None
        else:
            stock['Name']=i
            stock_final = stock_final.append(stock,sort=False)
    except Exception:
        None
print("Done")
# -------- WEB SCRAPER END ---------