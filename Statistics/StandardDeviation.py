from Statistics.Variance import get_variance
from Calculator.squared_root import square_root


def get_standard_deviation(data):
    value = get_variance(data)
    return round(square_root(value),1)