import pandas as pd
import matplotlib.pyplot as plt

class SMA:
    """
    Initialize the SMA class with given data and period.
    
    Parameters:
        data (list or numpy array): The input data for which SMA needs to be calculated.
        period (int): The period for which SMA needs to be calculated.
    """
    
    def __init__(self, data, period):
        self.sma = None
        self.data = pd.Series(data)
        self.period = period
        self.sma_values = []
        if len(self.data) > self.period:
            self.calculate()
        
    def calculate(self):
        """
        Calculate the Simple Moving Average (SMA).
        """
        sma = self.data.rolling(self.period).mean()
        self.sma = sma.iloc[self.period-1:]
        self.sma_values = sma
        
    def add_data_point(self, data_point):
        """
        Add a new data point to the existing data and recalculate the SMA.
        
        Parameters:
            data_point (float or int): The new data point to be added.
        """
        listTemp = self.data.values.tolist()
        listTemp.append(data_point)
        self.data = pd.Series(listTemp)
        if len(self.data) > self.period:
            self.calculate()
                    
    def get_smavalue(self):
        """
        Returns:
            float: The calculated SMA value.
        """
        return self.sma.iloc[-1]
    
    def plot_show(self):
        """
        Plot the SMA values calculated.
        """
        plt.plot(self.sma_values.values, label='SMA')
        plt.plot(self.data.values, label='Data')
        plt.legend(loc = 'upper left')
        plt.ylabel('SMA Values')
        plt.xlabel
        plt.title('SMA Chart - {} Period'.format(str(self.period)))
        plt.show()
            
prices = [44.12, 44.53, 44 , 43.61, 44.33, 44.83, 45.1 , 45.42, 45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28, 46 , 46.03, 46.41, 46.22, 45.64, 46.21, 46.25, 45.71, 46.45, 45.78, 45.35, 44.03, 44.18, 44.22, 44.57, 43.42, 42.66, 43.13]
sma = SMA(prices, 10)

# print(len(sma.data.values))
# print(sma.sma_values)
sma.add_data_point(43.13)
sma.add_data_point(43.12)
sma.add_data_point(43.10)
sma.add_data_point(43.22)
sma.add_data_point(43.43)
sma.add_data_point(43.41)
# print(len(sma.data.values))
# print(sma.sma_values)

sma.plot_show()