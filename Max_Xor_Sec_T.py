from sys import stdin

n = int(stdin.readline())

s = list(map(int, stdin.readline().split()))

lucky = 0 
stack = []

for i in s:
    while stack:
        lucky = max(lucky, stack[-1]^i)
        if i > stack[-1]:
            stack.pop()
        else:
            break
    stack.append(i)

print(lucky)