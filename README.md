# ILIB - Technical Indicator Library

![preview](preview.jpg)

ILIB is a library of technical indicators that can be used to build trading strategies. It is written in Python and uses the [Pandas](https://pandas.pydata.org/docs/) and [Numpy](https://numpy.org/doc/stable/) library for data manipulation and [Matplotlib](https://matplotlib.org/) for charting.

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/release/python-370/)
[![PyPI](https://img.shields.io/pypi/v/ilib)](https://pypi.org/project/ilib/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ilib)](https://img.shields.io/github/downloads/devthakker/ilib/total.svg)
![GitHub](https://img.shields.io/github/license/devthakker/ilib)

## Features

- Implements various popular technical indicators for financial analysis.
- Simple and intuitive API for easy integration into your trading systems.
- Supports Python 3.7 and above.
- Well-documented codebase and example usage for each indicator.


## Installation

```bash
pip install ilib
```

## Available Indicators

- [x] [Bollinger Bands](https://www.investopedia.com/terms/b/bollingerbands.asp)
- [x] [Commodity Channel Index](https://www.investopedia.com/terms/c/commoditychannelindex.asp)
- [x] [Exponential Moving Average](https://www.investopedia.com/terms/e/ema.asp)
- [x] [Moving Average Convergence Divergence](https://www.investopedia.com/terms/m/macd.asp)
- [x] [Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp)
- [x] [Simple Moving Average](https://www.investopedia.com/terms/s/sma.asp)
- [x] [Stochastic Oscillator](https://www.investopedia.com/terms/s/stochasticoscillator.asp)

## Usage

```python
import ilib as ti

#data 
prices = [45.15, 46.02, 45.89, 46.29, 45.94, 46.03, 45.71, 45.63, 45.36, 45.81, 46.10, 45.77, 45.95, 45.61, 45.27, 44.17, 44.12, 44.36, 44.54, 44.23, 44.29, 44.15, 44.34, 44.58, 44.69, 44.76, 44.62, 44.57, 44.45, 44.38, 44.23, 44.17, 44.04, 44.22, 44.57, 43.42, 42.66, 43.13, 43.43, 43.70, 43.88, 44.22]

#RSI
rsi = ti.rsi(14, prices)

print(rsi.get_rsi())

rsi.add_data(44.57)

print(rsi.get_rsi())
```
