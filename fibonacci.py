def fibonacci_recursive(n, fib=[1, 1]):
    if len(fib) >= n:
        return fib[:n]  
    fib.append(fib[-1] + fib[-2]) 
    return fibonacci_recursive(n, fib)

fib_numbers = fibonacci_recursive(5)
print(" ".join(map(str, fib_numbers)))


#OUTPUT
#1 1 2 3 5
