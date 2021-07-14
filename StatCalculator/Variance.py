from Calculator.Squared import squared
from Calculator.Subtraction import subtraction
from statistics import mean

#Variance is the average of the squared differences from the mean

def variance(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        data = [a, b, c, d, e]

        #find the mean
        var_mean = mean(data)

        #For each number, subtract the mean
        difference = []
        for item in data:
            difference.append(item-var_mean)

        #Square the results
        squared_results = []
        for item in difference:
            squared_results.append(item*item)

        #Take the average of the squared results
        results = (sum(squared_results))/(len(squared_results))

        return round(results, 2)

    except ZeroDivisionError:
        print("Error! Cannot divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")