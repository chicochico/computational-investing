# this is the script for the homework 1 of Computational Investing

import itertools

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da


# generate portfolio allocation combinations
ef gen_portfolio_allocations(symbols, resolution):
    alloc_values = np.arange(0., 1.+resolution, resolution)
    alloc_combinations = list(itertools.product(alloc_values, repeat=len(symbols)))
    alloc_combinations = pd.DataFrame(alloc_combinations, columns=symbols)
    return alloc_combinations[alloc_combinations.sum(1) == 1]

# simulate portfolio
def simulate_portfolio(start_date, end_date, symbols, allocation):
    timeofday = dt.timedelta(hours=16)

    close_prices = data_frame['close'].values
    normalized_close_prices = close_prices / close_prices[0, :]

    daily_returns = normalized_close_prices.copy()
    tsu.returnize0(daily_returns)

    portfolio_returns = np.sum(daily_returns * allocation, axis=1)
    portfolio_total = np.cumprod(portfolio_returns + 1)
    component_total = np.cumprod(daily_returns + 1, axis=0)

    plt.clf()
    fig = plt.figure()
    fig.add_subplot(111)
    plt.plot(timestamps, component_total, alpha=0.3)
    plt.plot(timestamps, portfolio_total)
    names = symbols
    names.append('Portfolio')
    plt.legend(names)
    plt.ylabel('Cumulative Returns')
    plt.xlabel('Date')
    fig.autofmt_xdate(rotation=45)
    return (daily_returns, portfolio_total)
