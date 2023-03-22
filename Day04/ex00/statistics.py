def ft_statistics(*args: any, **kwargs: any) -> None:
    """statistics"""
    c = 0
    try:
        for i in args:
            if (type(i) != int and len(args) == 0):
                raise TypeError("ERROR")
        for i in kwargs:
            if kwargs[i] == "mean":
                for i in args:
                    c += i
                if (len(args) == 0):
                    print("ERROR")
                    break
                c /= len(args)
                print("mean :", c)
            elif kwargs[i] == "median":
                n = sorted(args)
                if len(n) % 2 == 0:
                    median = (n[len(n) // 2] + n[len(n) // 2 - 1]) / 2
                else:
                    median = n[len(n) // 2]
                print("median :", median)
            elif kwargs[i] == "quartile":
                quartile = []
                n1, n2 = 0, 0
                n = sorted(args)
                # https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch11/median-mediane/5214872-fra.htm
                if len(n) % 2 == 0 and len(n) > 2:
                    n1 = (n[len(n) // 2] + n[len(n) // 2 - 1]) / 2
                    n2 = (n[len(n) // 2] + n[len(n) // 2 + 1]) / 2
                elif len(n) % 2 == 0 and len(n) <= 2:
                    n1 = n[len(n) // 2 - 1]
                    n2 = n[len(n) // 2]
                elif len(n) % 1 == 0 and len(n) <= 1:
                    n1 = n[len(n) // 2 - 1]
                    n2 = n[len(n) // 2]
                else:
                    n1 = float(n[len(n) // 2 - 1])
                    n2 = float(n[len(n) // 2 + 1])
                quartile = [n1, n2]
                print("quartile :", quartile)
            elif kwargs[i] == "std":
                m = args
                # https://www.statology.org/standard-deviation-of-list-python/
                val = (sum((x-(sum(m) / len(m)))**2 for x in m) / len(m))**0.5
                print("std :", val)
            elif kwargs[i] == "var":
                m = args
                mean = sum(m) / len(m)
                res = sum((i - mean) ** 2 for i in m) / len(m)
                print("var :", res)
            else:
                print("ERROR")
    except TypeError as e:
        print(e)
        exit()
    return
