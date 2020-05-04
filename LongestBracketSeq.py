s = input()

stack = []
count = 0
max_count = []
count_substring = 0

for i in s:
    if i == '(':
        count += 1
        stack.append(-1)
    elif i == ')':
        if stack:
            count += 1
            stack.pop()
        else:
            max_count.append(count)
            count = 0
    # print(count)

# if count:
#     max_count.append(count)

if max_count:
    max_substring = max(max_count)
    print(max_substring, max_count.count(max_substring))
else:
    print(0, 1)
