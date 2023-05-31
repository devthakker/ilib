import numpy as np

class CCI:
    """
    Calculate the Commodity Channel Index (CCI) of a stock.
    
    Parameters:
    data (list): A list of the stock prices in chronological order, with the most recent price last.
    period (int): The number of periods to use in the CCI calculation. Default is 20.
    factor (float): The factor used to scale the Mean Deviation (MD) in the CCI calculation. Default is 0.015.
    """
    
    def __init__(self, period=20, data=[], factor=0.015) -> None:
        self.cci = None
        self.data = data
        self.period = period
        self.factor = factor
        if len(data) > self.period:
            self.calculate_cci()

        
    def calculate_typical_price(self):
        """
        Calculate the typical price of a stock.
        
        Returns:
            float: The typical price of a stock.
        """
        return sum(self.data) / len(self.data)

    def calculate_mean_deviation(self, typical_price):
        """
        Calculate the mean deviation of a stock.
        
        Returns:
            float: The mean deviation of a stock.
        """
        deviations = [abs(price - typical_price) for price in self.data]
        return sum(deviations) / len(self.data)

    def calculate_cci(self):
        """
        Calculate the Commodity Channel Index (CCI) of a stock.
        Returns:
            null: The CCI is stored in the cci attribute.
        """
        typical_prices = [(high + low + close) / 3 for high, low, close in zip(self.data, self.data, self.data)]
        sma = sum(typical_prices[:self.period]) / self.period
        mean_deviations = [abs(typical_price - sma) for typical_price in typical_prices]
        mda = sum(mean_deviations[:self.period]) / self.period

        self.cci = [(typical_price - sma) / (0.015 * mda) for typical_price in typical_prices]
        
    def add_data_point(self, price):
        """
        Add a new price to the data list and recalculate the CCI.
        
        Parameters:
            price (float): The latest price.
        Returns:
            null: The CCI is stored in the cci attribute.
        """
        self.data.append(price)
        if len(self.data) > self.period:
            self.calculate_cci()
        
    def get_cci(self):
        """Return the current CCI value.

        Returns:
            float: The current CCI value.
        """
        return self.cci[-1]
        
