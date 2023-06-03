import matplotlib.pyplot as plt

class AverageTrueRange:
    """
    Average True Range (ATR) is a technical analysis indicator that measures market volatility by decomposing the entire range of an asset price for that period.
    
    Parameters:
        period (int): The period for which ATR needs to be calculated.
    """
    def __init__(self, period=14, high_prices=None, low_prices=None, close_prices=None):
        self.ATR = None
        self.ATR_values = []
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
            raise Exception("Not enough data points to calculate ATR")
        true_ranges = []
        for i in range(len(self.high_prices)-self.period,len(self.high_prices)):
            high_low_range = self.high_prices[i] - self.low_prices[i]
            high_close_range = abs(self.high_prices[i] - self.close_prices[i - 1])
            low_close_range = abs(self.low_prices[i] - self.close_prices[i - 1])
            true_range = max(high_low_range, high_close_range, low_close_range)
            true_ranges.append(true_range)
        self.ATR =  sum(true_ranges) / len(true_ranges)
        self.ATR_values.append(self.ATR)
        
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
            self.calculate()
    
    def get_ATR(self):
        """Return the current ATR value."""
        return self.ATR
    
    def plot_show(self):
        """Plot the ATR values."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.set_title('Stock Prices')
        ax1.plot(self.high_prices, label='High')
        ax1.plot(self.low_prices, label='Low')
        ax1.plot(self.close_prices, label='Close')
        ax1.legend(loc='upper left')
        ax2.set_title('ATR - {} period'.format(self.period))
        ax2.plot(self.ATR_values, label='ATR')
        plt.show()
        return
        
    def plot_save(self, filename):
        """Save the ATR values plot to a file."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.set_title('Stock Prices')
        ax1.plot(self.high_prices, label='High')
        ax1.plot(self.low_prices, label='Low')
        ax1.plot(self.close_prices, label='Close')
        ax1.legend(loc='upper left')
        ax2.set_title('ATR - {} period'.format(self.period))
        ax2.plot(self.ATR_values, label='ATR')
        plt.savefig(filename)
        plt.close()
        return
    
    
# prices = [44.12, 44.53, 44 , 43.61, 44.33, 44.83, 45.1 , 45.42, 45.84, 46.08, 45.89, 45.03, 45.61, 46.28, 46.28]
# added = [46 , 46.03, 46.41, 46.22, 45.64, 46.21, 46.25, 45.71, 46.45,  47.35, 45.90, 44.18, 44.22, 44.57, 43.42, 42.66, 43.13]

high_prices = [44.12, 44.53, 44 , 43.61, 44.33, 44.83, 45.1 , 45.42, 45.84, 46.08, 45.89, 45.03, 45.61, 46.28, 46.28]
low_prices = [43.11, 43.84, 43.11, 43.11, 43.61, 44.41, 44.23, 44.8 , 45.01, 45.62, 44.8 , 44.75, 45.2 , 45.75, 45.75]
close_prices = [43.84, 44.23, 43.34, 43.61, 44.23, 44.41, 44.8 , 44.84, 45.62, 45.89, 45.03, 44.75, 45.2 , 45.75, 46.03]

add_high = [46 , 46.03, 46.41, 46.22, 45.64, 46.21, 46.25, 45.71, 46.45,  47.35, 45.90, 44.18, 44.22, 44.57, 43.42, 42.66, 43.13]
add_low = [45.80, 45.21, 45.80, 45.90, 45.01, 45.61, 45.71, 45.61, 45.71, 46.22, 45.61, 43.61, 43.61, 43.61, 42.66, 42.66, 42.66]
add_close = [45.80, 45.61, 45.80, 45.90, 45.01, 45.61, 45.71, 45.61, 45.71, 46.22, 45.61, 43.61, 43.61, 43.61, 42.66, 42.66, 42.66]

ema = AverageTrueRange(10, high_prices, low_prices, close_prices)
for i in range(len(add_high)):
    ema.add_data_point(add_high[i], add_low[i], add_close[i])
    
print(ema.ATR_values)

ema.plot_show()