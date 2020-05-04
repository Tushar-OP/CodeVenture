t = int(input())

mx = [0]*31
mn = [0]*31

for i in range(1, 31):
    k = i // 2
    mn[i] = mn[k] + mn[i-k-1] + i+1
    mx[i] = mx[i-1] + mx[0] + i+1


for _ in range(t):
    n, m = map(int, input().split())

    if m < mn[n]:
        print(-1)
    elif m <= mx[n]:
        print(0)
    else:
        print(m - mx[n])
