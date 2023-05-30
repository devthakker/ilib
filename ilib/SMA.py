import pandas as pd

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
        if len(self.data) > self.period:
            self.calculate()
        
    def calculate(self):
        """
        Calculate the Simple Moving Average (SMA).
        """
        self.sma = self.data.rolling(self.period).mean()
        
    def add_data_point(self, data_point):
        """
        Add a new data point to the existing data and recalculate the SMA.
        
        Parameters:
            data_point (float or int): The new data point to be added.
        """
        self.data.append(data_point)
        self.data = self.data[-self.period:]
            
    def get_smavalue(self):
        """
        Returns:
            float: The calculated SMA value.
        """
        return self.sma.iloc[-1]
            
