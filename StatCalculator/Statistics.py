from Calculator.Calculator import Calculator
from StatCalculator.Mean import mean
from StatCalculator.Median import median
from StatCalculator.Mode import mode
from StatCalculator.Variance import variance
from StatCalculator.StandardDeviation import standard_deviation


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, a, b, c, d, e):
        self.result = mean(a, b, c, d, e)
        return self.result

    def median(self, a, b, c, d, e):
        self.result = median(a, b, c, d, e)
        return self.result

    def mode(self, a, b, c, d, e):
        self.result = mode(a, b, c, d, e)
        return self.result

    def variance(self, a, b, c, d, e):
        self.result = variance(a, b, c, d, e)
        return self.result

    def standard_deviation(self, a, b, c, d, e):
        self.result = standard_deviation(a, b, c, d, e)
        return self.result

    pass