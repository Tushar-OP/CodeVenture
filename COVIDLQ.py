from sys import stdin

try:
    T = int(stdin.readline())
except:
    T = 0

for _ in range(T):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().rstrip().split()))
    res = []
    for i in range(n):
        if arr[i] == 1:
            for j in range(i, n):
                print(i, j)
                if arr[j] == 1:
                    x = j - i
                    res.append(x)
                    i = j
        
    
    res2 = []
    for i in range(len(res)):
        if res[i] != 0:
            res2.append(res[i])

    if res2 ==[]: #if only 1 element was in the array i.e. arr = [1]
        print('YES')
    elif min(res2) >=6 :
        print('YES')
    else:
        print('NO')
    