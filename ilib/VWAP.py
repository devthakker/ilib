class VWAP:
    """
    VWAPCalculator is a class that calculates the volume weighted average price (VWAP) of a stock.
    
    Attributes:
        
        total_volume (int): The total volume of the stock.
        cumulative_price_volume (float): The cumulative price volume of the stock.
        cumulative_time_weighted_price_volume (float): The cumulative time weighted price volume of the stock.  
        moving_volume (int): The moving volume of the stock.
        moving_cumulative_price_volume (float): The moving cumulative price volume of the stock.
        vwap (float): The volume weighted average price of the stock.
        """
    def __init__(self, total_volume=0, cumulative_price_volume=0, cumulative_time_weighted_price_volume=0, moving_volume=0, moving_cumulative_price_volume=0):
        self.total_volume = total_volume
        self.cumulative_price_volume = cumulative_price_volume  
        self.cumulative_time_weighted_price_volume = cumulative_time_weighted_price_volume
        self.moving_volume = moving_volume
        self.moving_cumulative_price_volume = moving_cumulative_price_volume
        
        if self.total_volume > 0:
            self.calculate_vwap()
        else:
            self.vwap = None

    def calculate_vwap(self):
        """
        Calculates the volume weighted average price (VWAP) of a stock.
        """
        if self.total_volume == 0:
            return None
        vwap = self.cumulative_price_volume / self.total_volume
        self.vwap = vwap

    def calculate_twap(self, total_time):
        """
        Calculates the time weighted average price (TWAP) of a stock.
        """
        if self.cumulative_time_weighted_price_volume == 0:
            return None
        twap = self.cumulative_time_weighted_price_volume / (self.total_volume * total_time)
        return twap

    def calculate_mvwap(self, period):
        """
        Calculates the moving volume weighted average price (MVWAP) of a stock.
        """
        if self.moving_volume < period:
            return None
        mvwap = self.moving_cumulative_price_volume / self.moving_volume
        return mvwap
    
    def add_data_point(self, price, volume, timestamp):
        """
        Adds a data point to the VWAP calculator.
        """
        self.total_volume += volume
        self.cumulative_price_volume += price * volume
        self.cumulative_time_weighted_price_volume += price * volume * timestamp
        self.moving_volume += volume
        self.moving_cumulative_price_volume += price * volume
        self.calculate_vwap()
        
    def get_vwap(self):
        """
        Returns the volume weighted average price (VWAP) of a stock.
        """
        return self.vwap
    
    def plot_show(self):
        """
        Plot the CCI values calculated.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.set_title('Stock Prices')
        ax1.plot(self.data, label='High')
        ax1.legend(loc='upper left')
        ax2.set_title('CCI - {} period'.format(self.period))
        ax2.plot(self.cci, label='CCI')
        plt.tight_layout()
        plt.show()
        return
    
    def plot_save(self, filename):
        """
        Plot the CCI values calculated and save to file.
        
        Parameters:
            filename (str): The filename to save the plot to.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.set_title('Stock Prices')
        ax1.plot(self.data, label='High')
        ax1.legend(loc='upper left')
        ax2.set_title('CCI - {} period'.format(self.period))
        ax2.plot(self.cci, label='CCI')
        plt.tight_layout()
        plt.savefig(filename)
        return
        


high_prices = [44.12, 44.53, 44 , 43.61, 44.33, 44.83, 45.1 , 45.42, 45.84, 46.08, 45.89, 45.03, 45.61, 46.28, 46.28]
low_prices = [43.11, 43.84, 43.11, 43.11, 43.61, 44.41, 44.23, 44.8 , 45.01, 45.62, 44.8 , 44.75, 45.2 , 45.75, 45.75]
close_prices = [43.84, 44.23, 43.34, 43.61, 44.23, 44.41, 44.8 , 44.84, 45.62, 45.89, 45.03, 44.75, 45.2 , 45.75, 46.03]

add_high = [46 , 46.03, 46.41, 46.22, 45.64, 46.21, 46.25, 45.71, 46.45,  47.35, 45.90, 44.18, 44.22, 44.57, 43.42, 42.66, 43.13]
add_low = [45.80, 45.21, 45.80, 45.90, 45.01, 45.61, 45.71, 45.61, 45.71, 46.22, 45.61, 43.61, 43.61, 43.61, 42.66, 42.66, 42.66]
add_close = [45.80, 45.61, 45.80, 45.90, 45.01, 45.61, 45.71, 45.61, 45.71, 46.22, 45.61, 43.61, 43.61, 43.61, 42.66, 42.66, 42.66]

ema = CCI(10, high_prices)
for i in range(len(add_high)):
    ema.add_data_point(add_high[i])
    print(ema.get_cci())
    
print(ema.get_cci())

ema.plot_show()
