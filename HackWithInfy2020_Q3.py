from sys import stdin
from math import gcd

def calculateCost(a,b):
    cost = []
    n= len(a)
    for i in range(n):
        if a[i] == 1 or a[i] == 0:
            cost.append(b[i])
        for j in range(n - 1):
            if gcd(a[i], a[j + 1]) == 1:
                cost.append(b[j] + b[j + 1])
    
    if cost == []:
        return -1
    else:
        return (min(cost))

def main():
    n = int(stdin.readline())
    a = [None]*n
    b = [None]*n
    for i in range(n):
        a[i] = int(stdin.readline())
    for i in range(n):
        b[i] = int(stdin.readline())
    result = calculateCost(a,b)
    print(result)

if __name__ == "__main__":
    main()