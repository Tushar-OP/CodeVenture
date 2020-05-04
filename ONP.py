try:
    T = int(input())
except:
    T = 0

operator = {'+':1, '-':1, '*':2, '/':2, '^':3}


for _ in range(T):
    exp = list(str(input()))

    res = []
    stack = []

    for i in range(len(exp)):

        if exp[i].isalpha():
            res.append(exp[i])

        if exp[i] == '(':
            stack.append(exp[i])

        elif exp[i] == ')':
                while stack[-1] != '(':
                    res.append(stack.pop())  
                stack.pop()

        elif exp[i] in operator:
            if stack[-1] == '(':
                stack.append(exp[i])

            elif operator[exp[i]] <= operator[stack[-1]]:
                while operator[exp[i]] <= operator[stack[-1]]:
                    res.append(stack.pop())
                
            elif operator[exp[i]] > operator[stack[-1]]:
                stack.append(exp[i])

        
    print(*res, sep='')
 