"""
@ Quant, 2020.
@ Anton Normelius

Python interface for available indicators.

"""
import time
import numpy as np 

from quant.indicators.trend import *
from quant.indicators.volatility import *
from quant.indicators.momentum import *
from quant.indicators.volume import *
from quant.indicators.stat import *

# Trend interface
# ---------------
def sma(data, period):
    """
    Compute trailing simple moving average with the specified period.
    
    Parameters
    ----------
    data : list
        Numpy array containing the data to be used.
    period : int
        Number of periods to be used.
    
    Returns
    -------
    list
        Returns a numpy ndarray with calculated simple moving averages.
    """
    return sma_calc(data, period)

def ema(data, periods):
    return ema_calc(data, periods)

def dema(data, periods):
    return dema_calc(data, periods)

def tema(data, periods):
    return tema_calc(data, periods)

def t3(data, periods, volume_factor = 0.7):
    return t3_calc(data, periods, volume_factor)

def tma(data, periods):
    return tma_calc(data, periods)

def smma(data, periods):
    return smma_calc(data, periods)

def lwma(data, periods):
    return lwma_calc(data, periods)

def wc(data, highs, lows):
    return wc_calc(data, highs, lows)

# Volatility interface
# --------------------
def bbands(data, periods, deviation = 2):
    return bbands_calc(data, periods, deviation)

def kc(close, high, low, period = 20, period_atr = 20, deviation = 2):
    return kc_calc(close, high, low, period, period_atr, deviation)


def atr(prices, highs, lows, periods):
    return atr_calc(prices, highs, lows, periods)

def cv(highs, lows, period = 10, smoothing_period = 10):
    """ 
    Chaikin Volatility

    :param highs: High values
    :type highs: ndarray
    :param lows: Low values
    :type lows: ndarray
    :param period: Number of periods when calculating the ema, default to 10.
    :type period: int
    :param smoothing_period: Number of periods when smoothing the ema, default to 10.
    :type smoothing_period: int
    :return: Returns a ndarray with calculated chaikin volatility prices.
    :rtype: ndarray.float64
    """
    return cv_calc(highs, lows, period, smoothing_period)

# Momentum interface
# -----------------
def rsi(data, periods, rsi_type = "smoothed"):
    return rsi_calc(data, periods, rsi_type.lower())

def macd(data):
    return macd_calc(data)

def willr(data, highs, lows, periods):
    return willr_calc(data, highs, lows, periods)

def roc(data, periods):
    return roc_calc(data, periods)

def vpt(data, volumes):
    return vpt_calc(data, volumes)

def mi(data, periods):
    return mi_calc(data, periods)

def apo(data, period_slow = 26, period_fast = 12, ma = "sma"):
    
    if ma.lower() not in ["sma", "ema"]:
        raise ValueError("param 'ma' needs to be 'ema' or 'sma'")

    return apo_calc(data, period_slow, period_fast, ma.lower())

def bop(high, low, open_, close):
    return bop_calc(high, low, open_, close)

def cmo(close, period):
    return cmo_calc(close, period)

def mfi(high, low, close, volume, period):
    return mfi_calc(high, low, close, volume, period)

def ppo(prices, period_fast = 12, period_slow = 26, ma_type = "ema"):
    if ma_type.lower() not in ["sma", "ema"]:
        raise ValueError("Param 'ma_type' needs to be 'sma' or 'ema'")

    return ppo_calc(prices, period_fast, period_slow, ma_type)

#def stochastic(close, high, low, mode = "fast", period_k = 10, method = "ema"):
#    """
#    Returns %K and %D stochastics.
#
#    :param close: Closing prices.
#    :type close: List.
#    :param high: High prices.
#    :type high: List.
#    :param low: Low prices.
#    :type low: List.
#    :param mode: Specify whether to calculate 'fast' or 'slow' stochastic.
#    :type mode: Str.
#    :param period_k: Specify the number of periods used in the Stochastic (%K)
#        calculation.
#    :type period_k: Int.
#    :param method: Specify the method that is used to calculate Stochastic (%D) 
#        calculation.
#    :type method: Str.
#    :return tuple: A tuple containing (%K, %D).
#    """
#    if method and method.lower() not in ['sma', 'ema']:
#        raise ValueError("Param 'method' needs to be 'sma' or 'ema'.")
#    
#    if mode and mode.lower() not in ['fast', 'slow']:
#        raise ValueError("Param 'mode' needs to be 'fast' or 'slow'.")
#    
#    if not isinstance(period_k, int):
#        raise ValueError("Param 'period_k' needs to be an int.")
#
#    return stochastic_calc(close, high, low, mode, period_k, method)


def cci(close, high, low, period = 20):
    return cci_calc(close, high, low, period)

def aroon(high, low, period = 20):
    return aroon_calc(high, low, period)

#def tsi(close, period = 25, period_double = 13):
#    return tsi_calc(close, period, period_double)


# Volume interface
# ---------------
def acdi(prices, highs, lows, volumes):
    return acdi_calc(prices, highs, lows, volumes)

def obv(prices, volumes):
    return obv_calc(prices, volumes)

def cmf(prices, highs, lows, volumes, periods = 21):
    return cmf_calc(prices, highs, lows, volumes, periods)

def ci(prices, highs, lows, volumes):
    return ci_calc(prices, highs, lows, volumes)

def pvi(prices, volumes):
    return pvi_calc(prices, volumes)

def nvi(prices, volumes):
    return nvi_calc(prices, volumes)


# Stat interface
# -------------

def std(data, period, normalize = True):
    return std_calc(data, period, normalize)

def var(data, period, normalize = True):
    return var_calc(data, period, normalize)

def cov(data, market, period, normalize = True):
    return cov_calc(data, market, period, normalize)

def beta(prices, market, period, normalize = False):
    return beta_calc(prices, market, period, normalize)

def pct_change(prices, period):
    return pct_change_calc(prices, period)

# SSE TESTING
#def sse(price, high, low):
#    return sse_calc(price, high, low);



