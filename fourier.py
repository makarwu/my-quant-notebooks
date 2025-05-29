def address(ticker):
    key = '3GJzfde4UvWFwJV3X6UM0Up7IBP92zMs'
    return f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={key}'

import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Rk(prices):
    N = len(prices)
    result = []
    for k in range(N):
        total = 0
        for n in range(N):
            total += prices[n]*np.exp(1j*(-2*np.pi*k*n/N))
        result.append(total)
    return result

def fRk(N, d=1.0):
    return [k/(N*d) if k <= N / 2 else (k-N)/(N*d) for k in range(N)]

def iRk(prices):
    N = len(prices)
    result = []
    for k in range(N):
        total = 0
        for n in range(N):
            total += prices[n]*np.exp(1j*(2*np.pi*k*n/N))
        result.append(total / N)
    return result

def Data(ticker, days=150):
    resp = requests.get(address(ticker)).json()
    #resp.raise_for_status()
    df = pd.DataFrame(resp["historical"])[::-1]
    prices = df["adjClose"].values.tolist()[-days:]
    return prices

ticker = "NVDA"
close = Data(ticker)
#print(close)

x = list(range(len(close)))
fft = Rk(close)
fltr = fRk(len(fft))

fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot(111)

for alpha in np.arange(0, 0.201, 0.001):
    fft_fit = fft[:]
    for i, value in enumerate(fltr):
        if abs(value) > alpha:
            fft_fit[i] = 0

    fy = iRk(fft_fit)
    ax.cla()
    title = 'Stock: {} | Alpha: {}'.format(ticker, alpha)
    ax.set_title(title)
    ax.plot(x, close, color="blue")
    ax.plot(x, fy, color="red", linewidth="0.8")
    plt.pause(0.1)

plt.show()
