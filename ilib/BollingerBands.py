import numpy as np
import pandas as pd

class BollingerBands:
    """
    Initialize the BollingerBands class with given data, window size, and number of standard deviations.
        
    Parameters:
        data (list or numpy array): The input data for which Bollinger Bands need to be calculated.
        window (int, optional): The size of the moving window. Default is 20.
        num_std (int, optional): The number of standard deviations for the Bollinger Bands. Default is 2.
    """
    def __init__(self, window=20, num_std=1, data=None):
        if data is None:
            self.data = []
        else :
            self.data = data
        self.window = window
        self.num_std = num_std
        self.upper_band = []
        self.middle_band = []
        self.lower_band = []
        if len(self.data) > 20:
            self.calculate()
    
    def calculate(self):
        """
        Calculate the Bollinger Bands.
        
        """
        data = pd.DataFrame(self.data)
        rolling_mean = data.rolling(window=self.window).mean()
        rolling_std = data.rolling(window=self.window).std()
        self.upper_band.append(rolling_mean + (self.num_std * rolling_std))
        self.middle_band.append(rolling_mean)
        self.lower_band.append(rolling_mean - (self.num_std * rolling_std))
        return
    
    def add_data_point(self, new_data_point):
        """
        Add a new data point to the existing data.
        
        Parameters:
            new_data_point (float or int): The new data point to be added.
        """
        self.data.append(new_data_point)
        if self.upper_band is not None:
            self.calculate()
        return
            
    def get_BollingerBands(self):
        """
        Returns the current Bollinger Bands values.
        
        Returns:
            tuple: A tuple containing three current values for: upper_band, middle_band, and lower_band.
        """
        return (float(self.upper_band.values[-1]), float(self.middle_band.values[-1]), float(self.lower_band.values[-1]))
    
    def plot_show(self):
        """
        Plot the Bollinger Bands calculated.
        """
        import matplotlib.pyplot as plt
        plt.figure(figsize=(12,6))
        plt.plot(self.data, label='Price')
        plt.plot(self.upper_band, label='Upper Band')
        plt.plot(self.middle_band, label='Middle Band')
        plt.plot(self.lower_band, label='Lower Band')
        plt.legend(loc='upper left')
        plt.show()
        return
    
prices = [44.12, 44.53, 44 , 43.61, 44.33, 44.83, 45.1 , 45.42, 45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28]
added = [46 , 46.03, 46.41, 46.22, 45.64, 46.21, 46.25, 45.71, 46.45, 45.78, 45.35, 44.03, 44.18, 44.22, 44.57, 43.42, 42.66, 43.13]

ema = BollingerBands(10, prices)
for i in added:
    ema.add_data_point(i)
    
ema.plot_show()



