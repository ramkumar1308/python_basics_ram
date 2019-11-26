def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid number")
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        for i in range(1,n+1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(9))


#0 1 1 2 3 5 8 13 21