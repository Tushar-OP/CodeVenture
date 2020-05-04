from sys import stdin, stdout

try:
    T = int(stdin.readline())
except:
    T = 0

for _ in range(T):
    n = int(stdin.readline())
    lst = list(map(int, stdin.readline().rstrip().split()))

    idx = -111
    for i in range(n-2, -1, -1):
        if lst[i] < lst[i + 1]:
            idx = i
            break
    if idx == -111:
        print(-1)
        continue

    j = idx + 1
    while j < n:
        if lst[j] <= lst[idx]:
            break
        j +=1

    lst[idx], lst[j - 1] = lst[j - 1], lst[idx]

    lst2 = lst[idx + 1:]
    lst2.sort()
    res = lst[:i + 1] + lst2[:]
    print(*res, sep='')
