def ft_statistics(*args: any, **kwargs: any) -> None:

    c = 0;
    for i in kwargs:
        if kwargs[i] == "mean":
            for i in args:
                c += i
            c /= len(args)
            print ("mean :", c)
        elif kwargs[i] == "median":
            numbers = sorted(args)
            if len(numbers) % 2 == 0:
                median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
            else:
                median = numbers[len(numbers) // 2]
            print ("median :", median)
            
                

        # elif kwargs[i] == "quartile":
            
    

        # if e == "median":
        # if e == "quartile":
    return