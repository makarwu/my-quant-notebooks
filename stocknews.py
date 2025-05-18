def FMPNews(page=0, size=5):
    key = '3GJzfde4UvWFwJV3X6UM0Up7IBP92zMs'
    return f'https://financialmodelingprep.com/api/v3/fmp/articles?page={page}&size={size}&apikey={key}'

import requests
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
import time 

# Display all rows
pd.set_option('display.max_rows', None)

# Display all columns
pd.set_option('display.max_columns', None)

pages = 5
size = 500

url = FMPNews(size=2)
resp = requests.get(url).json()

print(resp)