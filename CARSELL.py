from sys import stdin

try:
    T = int(stdin.readline())
except:
    T = 0

for _ in range(T):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().rstrip().split()))
    arr.sort(reverse = True)
    
    cost = []
    for i in range(n):
        i = 0
        # if arr == []:
        #     break
        
        x = arr[i]
        cost.append(x)
        arr.pop(i)
        i = 0

        for j in range(len(arr)):
            arr[j] = arr[j] - 1
    
    cost = sum( [i for i in cost if i>0]) % 1000000007
    print(cost)