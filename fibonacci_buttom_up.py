def fibonacci(order):
    if order <= 0:
        raise ValueError('The order is 0 or under 0") 
    elif order == 1 or order == 2:
        return 1
    else:
        buttom_up = [None] * (order+1)
        buttom_up[1] = 1
        buttom_up[2] = 1
        for i in range(3, len(buttom_up)):
            buttom_up[i] = buttom_up[i-1] + buttom_up[i-2]
        return buttom_up[order]
    
print(fibonacci(1000))
