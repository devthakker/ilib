class STOCHOSCILLATOR:
    def __init__(self, period, smoothing_period, oversold_threshold, overbought_threshold,high_prices=None, low_prices=None, close_prices=None):
        self.stoch = None
        self.smoothed = None
        self.period = period
        self.smoothing_period = smoothing_period
        self.oversold_threshold = oversold_threshold
        self.overbought_threshold = overbought_threshold
        self.high_prices = high_prices if high_prices is not None else []
        self.low_prices = low_prices if low_prices is not None else []
        self.close_prices = close_prices if close_prices is not None else []
        if len(self.high_prices) > self.period and len(self.low_prices) > self.period and len(self.close_prices) > self.period:
            self.calculate()

    def add_data(self, high, low, close):
        self.high_prices.append(high)
        self.low_prices.append(low)
        self.close_prices.append(close)
        if len(self.high_prices) > self.period:
            self.high_prices = self.high_prices[-self.period:]
            self.low_prices = self.low_prices[-self.period:]
            self.close_prices = self.close_prices[-self.period:]

    def calculate(self):
        if len(self.high_prices) < self.period:
            return None
        highest_high = max(self.high_prices)
        lowest_low = min(self.low_prices)
        latest_close = self.close_prices[-1]
        stochastic_value = (latest_close - lowest_low) / (highest_high - lowest_low) * 100

        if len(self.close_prices) >= self.smoothing_period:
            smoothed_stochastic = sum(self.close_prices[-self.smoothing_period:]) / self.smoothing_period
        else:
            smoothed_stochastic = None

        self.stoch, self.smoothed =  stochastic_value, smoothed_stochastic

    def is_oversold(self, stochastic_value):
        return stochastic_value <= self.oversold_threshold

    def is_overbought(self, stochastic_value):
        return stochastic_value >= self.overbought_threshold
    
    def get_stoch(self):
        return self.stoch
    
    def get_smoothed(self):
        return self.smoothed
