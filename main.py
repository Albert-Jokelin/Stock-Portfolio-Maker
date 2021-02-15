# This program is designed by Albert Jokelin.
# This program takes data from the NSE and BSE and makes a highly profitable portfolio
# To get the latest csv file, go to https://www1.nseindia.com/products/content/sec_bhavdata_full.csv
# This project has been built for educational purposes, DO NOT use this to make your portfolio choices
# If you use this software, any liability it brings will solely be your responisibiliy

# Import required libraries
import pandas as pd
import numpy as np
import requests
import csv

#Load Data
f = open("NSE_DATA.csv", "r")
nse_list = list(csv.reader(f))