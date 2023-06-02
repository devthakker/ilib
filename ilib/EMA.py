import numpy as np
import matplotlib.pyplot as plt

class EMA:
    def __init__(self, window, data=None):
        """
        Initialize the EMA class with given data and window size.
        
        Parameters:
            data (list or numpy array): The input data for which EMA needs to be calculated.
            window (int): The size of the window for calculating EMA.
        """
        self.ema = None
        self.ema_values = []
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
    
    def plot_show(self):
        """
        Plot the EMA values calculated.
        """
        plt.plot(self.ema, label='EMA')
        plt.plot(self.data, label='Data')
        plt.legend(loc = 'upper left')
        plt.ylabel('EMA Values')
        plt.xlabel
        plt.title('EMA Chart - {} Period'.format(str(self.window)))
        plt.show()
        return
    
    def plot_save(self, filename):
        """
        Plot the EMA values calculated and save the plot to a file.
        
        Parameters:
            filename (str): The name of the file to save the plot to.
        """
        plt.plot(self.ema, label='EMA')
        plt.plot(self.data, label='Data')
        plt.legend(loc = 'upper left')
        plt.ylabel('EMA Values')
        plt.xlabel
        plt.title('EMA Chart - {} Period'.format(str(self.window)))
        plt.savefig(filename)
        return
    
prices = [44.12, 44.53, 44 , 43.61, 44.33, 44.83, 45.1 , 45.42, 45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28]
added = [46 , 46.03, 46.41, 46.22, 45.64, 46.21, 46.25, 45.71, 46.45, 45.78, 45.35, 44.03, 44.18, 44.22, 44.57, 43.42, 42.66, 43.13]

ema = EMA(10, prices)
for i in added:
    ema.add_data_point(i)
    
ema.plot_show()
