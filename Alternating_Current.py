s = input()

stack = []

for i in s:
    if stack and i == stack[-1]:
        stack.pop()
    else:
        stack.append(i)

if stack:
    print('No')
else:
    print('Yes')
