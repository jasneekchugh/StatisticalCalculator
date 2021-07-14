def median(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        median_list = [a, b, c, d, e]
        length = len(median_list)
        sorted_median_list = sorted(median_list)
        return sorted_median_list[2]
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")