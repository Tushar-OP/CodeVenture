t = int(input())

symbols = []

res = []

for i in range(t):
    symbols.append(input())


for z in range(t):

    symbol = symbols[z]

    stack = []

    postfix = []

    priority = {'+':1,
                '-':1,
                '*':2,
                '/':2,
                '^':3,
                '-1':0
    }

    for i in range(len(symbol)):
        if symbol[i].isalpha():
            postfix.append(symbol[i])
        else:
            if symbol[i] == '(':
                stack.append(-1)
            elif symbol[i] == ')':
                j = len(stack)
                while stack[j-1] != -1:  
                    new = stack[-1]
                    stack.pop()
                    postfix.append(new)
                    j -= 1
                stack.pop()

            else:
                if priority[str(symbol[i])] > priority[str(stack[-1])]:
                    stack.append(symbol[i])
                else:
                    while priority[symbol[i]] <= priority[stack[-1]]:
                        new = stack[-1]
                        stack.pop()
                        postfix.append(new)

        # print(stack)
        # print(postfix)
    
    res.append(postfix)

for i in range(t):
    print(*res[i], sep="")




                


