from sys import stdin

count = 0
N = []
lsts = []

while(True):
    n = int(input())
    if n != 0:
        N.append(n)
    else:
        break

    lsts.append(list(map(int, stdin.readline().split())))

    count += 1

for z in range(count):

    lst = lsts[z]
    n = N[z]
    order = 1
    i = 0
    narrow_street = [0]
    approach_street = []

    while (i < n):
        if lst[i] == order:
            approach_street.append(lst[i])
            order += 1
        elif narrow_street[-1] == order:
            approach_street.append(narrow_street[-1])
            narrow_street.pop()
            order += 1
            i -= 1
        else:
            narrow_street.append(lst[i])

        i += 1

        
    del narrow_street[0]
    if narrow_street != []:
        approach_street.extend(narrow_street[::-1])

    
    flag = False
    for i in range(n):
        if approach_street[i] != i+1:
            flag = True
            break
    
    if flag:
        print('no')
    else:
        print('yes')
