import numpy as np

class StochRSICalculator:
    """
    StochRSICalculator is a class that calculates the Stochastic RSI (StochRSI) indicator.

    Args:
        period (int): The number of data points to consider for calculating the StochRSI.
        rsi_period (int): The number of data points to consider for calculating the RSI.
        k_period (int): The number of data points to consider for calculating the StochRSI %K value.
    """

    def __init__(self, period, rsi_period, k_period, prices=None):
        self.period = period
        self.rsi_period = rsi_period
        self.k_period = k_period
        self.prices = [] if prices is None else prices
        self.rsi_values = []
        self.k_values = []

    def calculate(self):
        """
        Calculates the StochRSI based on the added price data.

        Returns:
            float or None: The calculated StochRSI %K value. Returns None if there is insufficient data.
        """
        if len(self.prices) < self.period:
            return None

        # Calculate RSI
        changes = np.diff(self.prices)
        gains = np.where(changes > 0, changes, 0)
        losses = np.where(changes < 0, -changes, 0)
        avg_gain = np.mean(gains[:self.rsi_period])
        avg_loss = np.mean(losses[:self.rsi_period])
        for change in changes[self.rsi_period:]:
            avg_gain = (avg_gain * (self.rsi_period - 1) + max(change, 0)) / self.rsi_period
            avg_loss = (avg_loss * (self.rsi_period - 1) + abs(min(change, 0))) / self.rsi_period
        rsi = 100 - (100 / (1 + avg_gain / avg_loss))

        # Calculate StochRSI
        self.rsi_values.append(rsi)
        if len(self.rsi_values) > self.k_period:
            self.rsi_values = self.rsi_values[-self.k_period:]
        k_value = (rsi - min(self.rsi_values)) / (max(self.rsi_values) - min(self.rsi_values))
        self.k_values.append(k_value)

        return k_value
    
    def add_data_point(self, price):
        """
        Adds a new price data point to the calculator.

        Args:
            price (float): The price data point to be added.
        """
        self.prices.append(price)
        if len(self.prices) > self.period:
            self.prices = self.prices[-self.period:]
            self.calculate()

    def get_k_values(self):
        """
        Returns the list of calculated StochRSI %K values.

        Returns:
            list: List of StochRSI %K values.
        """
        return self.k_values
