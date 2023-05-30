import numpy as np

class EMA:
    def __init__(self, window, data=None):
        """
        Initialize the EMA class with given data and window size.
        
        Parameters:
            data (list or numpy array): The input data for which EMA needs to be calculated.
            window (int): The size of the window for calculating EMA.
        """
        self.ema = None
        if data is None:
            data = []
        else :
            self.data = data
        self.window = window
        if len(data) > window:
            self.calculate()
    
    def calculate(self, alpha=0.2):
        """
        Calculate the Exponential Moving Average (EMA) with the given alpha (smoothing factor).
        
        Parameters:
            alpha (float, optional): The smoothing factor. Default is 0.2.
        
        Returns:
            numpy array: The calculated EMA values.
        """
        data = np.array(self.data)
        self.ema = [data[0]]  # EMA for the first data point is the same as the data point itself
        for i in range(1, len(data)):
            ema = (alpha * data[i]) + ((1 - alpha) * self.ema[-1])
            self.ema.append(ema)
        self.ema = np.array(self.ema)
    
    def add_data_point(self, new_data_point, alpha=0.2):
        """
        Add a new data point to the existing data and recalculate the EMA.
        
        Parameters:
            new_data_point (float or int): The new data point to be added.
            alpha (float, optional): The smoothing factor. Default is 0.2.
        """
        self.data.append(new_data_point)
        if self.ema is not None:
            self.calculate(alpha)

    def get_EMA(self):
        """
        Returns:
            numpy array: The calculated EMA values.
        """
        return self.ema[-1]
    
