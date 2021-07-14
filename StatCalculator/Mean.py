from Calculator.Addition import addition
from Calculator.Division import division

def mean(a, b, c, d, e):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       d = int(d)
       e = int(e)
       total = a + b + c + d + e
       result = division(5, total)
       return result

    except ZeroDivisionError:
        print("Error! Cannot divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")
