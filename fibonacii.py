def fibonaci(n):
    if n<0:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)


for j in range(0,10):
    print(fibonaci(j))
