def printOperationTable(f, h, w):
    for i in range(1, h+1):
        print(*(f(i, k) for k in range(1, w+1)))