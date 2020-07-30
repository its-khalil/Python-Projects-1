def fib(order):
    if order <= 0:
        raise ValueError("The order is 0 or under 0")
    elif order == 1 or order == 2:
        return 1
    elif order == 0:
        return 0
    else:
        return fib(order-1) + fib(order-2)

print(fib(40))
    
