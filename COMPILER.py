try: 
    T = int(input())
except:
    T = 0


for _ in range(T):
    exp = list(input())
    stack = []
    r = 0

    for i in exp:
        if i == '<':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                r += 2
    
    print(r)

   