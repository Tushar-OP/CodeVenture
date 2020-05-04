N = []
t = 0
while(True):
    n = str(input().strip())
    if '-' in n:
        break
    else:
        t += 1
        N.append(n)

for z in range(t):

    seq = list(N[z])
    # print(seq)
    steps = 0
    stack = []

    for i in range(-1, -len(seq), -1):
        if seq[i] == '{':
            if stack:
                while stack[-1] != -1:
                    stack.pop()
                stack.pop()
            else:
                steps += 1
                seq[i] = '}'
                stack.append(-1)
        else:
            stack.append(-1)

    count_open = seq.count('{')
    count_close = seq.count('}')
    half = int(len(seq) / 2)
    if count_open > half:
        steps += (count_open-half)
    elif count_close > half:
        steps += (count_close-half)

    print(z+1,". ",steps, sep="")


        
