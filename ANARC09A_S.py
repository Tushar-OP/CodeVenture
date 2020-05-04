N = []
t = 0
while(True):
    n = str(input().strip())
    if '-' in n:
        break
    else:
        t += 1
        N.append(n)

for i in range(t):
    str_lst = list(N[i])
    c = 0
    stack = []
    
    for j in range(-1, -len(str_lst)-1, -1):
        if str_lst[j] == '{':
            if stack != []:
                while(stack[-1] != -1):
                    stack.pop()
                stack.pop()
            else:
                c += 1
                str_lst[j] = '}'
                stack.append(-1)
        elif str_lst[j] == '}':
            stack.append(-1)
    
    count_of_opening_brace = str_lst.count('{')
    count_of_closing_brace = str_lst.count('}')

    c += max(count_of_closing_brace, count_of_opening_brace) - (len(str_lst) / 2)

    print(i+1,". ", int(c), sep= "")


