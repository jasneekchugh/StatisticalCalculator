from Calculator.squared_root import squared_root
from StatCalculator.Variance import variance

def standard_deviation(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(d)

        #Find the variance
        stdev_variance = variance(a, b, c, d, e)

        #Take the square root
        result = squared_root(stdev_variance)
        return round(result, 2)

    except ZeroDivisionError:
        print("Error! Cannot divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")