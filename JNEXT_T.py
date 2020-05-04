t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    idx = -999
    for i in range(n-2,-1,-1):
        if lst[i] < lst[i+1]:
            idx = i
            break

    if idx == -999:
        print(-1)
        continue
    j = idx + 1
    while j < n:
        if lst[j] <= lst[idx]:
            break
        j += 1

    lst[idx] , lst[j-1] = lst[j-1], lst[i]
    arr = lst[idx+1:]
    arr.sort()
    res = lst[:i+1] + arr[:]
    print(*res,sep = "")
