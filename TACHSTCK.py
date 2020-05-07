n, d = map(int, input().rstrip().split())

n_list = []
for i in range(n):
    n_list.append(int(input()))

i = 0
res = 0

n_list.sort()

while (i < n-1):
    if n_list[i+1]-n_list[i] <= d:
        res += 1
        i += 1
        
    i += 1

print(res)