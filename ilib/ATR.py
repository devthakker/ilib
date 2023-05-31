class AverageTrueRange:
    """
    Average True Range (ATR) is a technical analysis indicator that measures market volatility by decomposing the entire range of an asset price for that period.
    
    Parameters:
        period (int): The period for which ATR needs to be calculated.
    """
    def __init__(self, period=14, high_prices=None, low_prices=None, close_prices=None):
        self.ATR = None
        self.period = period
        self.high_prices = high_prices if high_prices is not None else []
        self.low_prices = low_prices if low_prices is not None else []
        self.close_prices = close_prices if close_prices is not None else []
        if len(self.high_prices) > self.period:
            self.calculate()

    def calculate(self):
        """
        Calculate the Average True Range (ATR) of a stock.
        """
        if len(self.high_prices) < self.period:
            return None
        true_ranges = []
        for i in range(len(self.high_prices)):
            high_low_range = self.high_prices[i] - self.low_prices[i]
            high_close_range = abs(self.high_prices[i] - self.close_prices[i - 1])
            low_close_range = abs(self.low_prices[i] - self.close_prices[i - 1])
            true_range = max(high_low_range, high_close_range, low_close_range)
            true_ranges.append(true_range)
        self.ATR =  sum(true_ranges) / len(true_ranges)
        
    def add_data_point(self, high, low, close):
        """
        Add a new price to the data list and recalculate the ATR.
        
        Parameters:
            high (float): The latest high price.
            low (float): The latest low price.
            close (float): The latest close price.
            
        Returns:
            null: The ATR is stored in the ATR attribute."""
            
        self.high_prices.append(high)
        self.low_prices.append(low)
        self.close_prices.append(close)
        if len(self.high_prices) > self.period:
            self.high_prices = self.high_prices[-self.period:]
            self.low_prices = self.low_prices[-self.period:]
            self.close_prices = self.close_prices[-self.period:]
            self.calculate()
    
    def get_ATR(self):
        """Return the current ATR value."""
        return self.ATR
    