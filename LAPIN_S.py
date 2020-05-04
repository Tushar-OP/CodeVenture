# cook your dish here
import collections
try:
    T = int(input())
except:
    T = 0
S_arr = []    
for t in range(T):
    S_arr.append(str(input()))

for i in range(T):
    s_lst = list(S_arr[i])
    left = []
    right =[]
    if len(S_arr[i]) % 2 == 0:
        index = int(len(S_arr[i]) / 2)
        for j in range(index):
            left.append(s_lst[j])
        for j in range(index, len(s_lst)):
            right.append(s_lst[j])
    else:
        index = int(len(S_arr[i]) / 2 )
        # print(index)
        for j in range(index):
            left.append(s_lst[j])
        for j in range(index+1, len(s_lst)):
            right.append(s_lst[j])
    
    if collections.Counter(left) == collections.Counter(right) :
        print("YES")
    else:
        print("NO")
    