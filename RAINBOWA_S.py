from sys import stdin, stdout

try:
    T = int(stdin.readline())
except:
    T = 0
for t in range(T):
    N = int(stdin.readline())
   
    A = list(map(int, stdin.readline().rstrip().split()))
    
    inverse_A = A[::-1]
    Rainbow = [1, 2, 3, 4, 5, 6, 7]
    rem_duplicates = []

    for i in range(N):
        if A[i]  not in rem_duplicates:
            rem_duplicates.append(A[i])

    f = 0
    if max(A) == 7:
        if inverse_A == A:
            if rem_duplicates == Rainbow:
                f = 1

    if(f == 1):
        print('yes')
    else:
        print('no')
