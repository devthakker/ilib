class RSI:
    
    """
    Calculates the Relative Strength Index (RSI) of a stock based on its historical price data.

    Parameters:
    period (int): Number of periods to use for RSI calculation. Default is 14.
    data (list): A list of the stock prices in chronological order, with the most recent price last.
    
    Returns:
    rsi (float): The RSI of the stock.
    """
    
    def __init__(self, period=14, data=None):
        self.period = period
        self.rsi = None

        if data is None:
            self.data = []
        else:
            self.data = data
            if len(self.data) > self.period:
                self.calculate_rsi()

    def add_data_point(self, value):
        """
        Add a new price to the data list and calculate the new RSI.
        """
        self.data.append(value)
        if(len(self.data) > self.period):
            self.calculate_rsi()

    def calculate_rsi(self):
        """
        Calculate the RSI of the stock based on its historical price data.
        """
        if len(self.data) <= self.period:
            raise ValueError("Insufficient data to calculate RSI.")

        gains = []
        losses = []

        for i in range(1, len(self.data)):
            price_diff = self.data[i] - self.data[i - 1]
            if price_diff > 0:
                gains.append(price_diff)
                losses.append(0)
            elif price_diff < 0:
                losses.append(abs(price_diff))
                gains.append(0)
            else:
                gains.append(0)
                losses.append(0)

        avg_gain = sum(gains) / self.period
        avg_loss = sum(losses) / self.period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        self.rsi = rsi
        
    def get_rsi(self):
        """
        Return the current RSI value."""
        return self.rsi

    