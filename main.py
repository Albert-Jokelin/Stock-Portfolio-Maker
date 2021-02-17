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


try:
    df = pd.read_csv('C:\\scrapper.csv')
except Exception:
    print("CSV file not found")

