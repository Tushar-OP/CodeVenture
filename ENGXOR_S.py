from sys import stdin, stdout
try:
    T = int(stdin.readline())
except:
    T = 0

for t in range(T):
    N, Q = map(int, stdin.readline().rstrip().split())
    A = [bin(i).count("1") for i in list(map(int, stdin.readline().rstrip().split()))]

    P_arr = []
    for q in range(Q):
        P = int(stdin.readline())
        P_arr.append(bin(P).count("1"))

    even = 0
    odd = 0

    for i in range(N):
        if A[i] % 2 == 0:
            even += 1
    odd = N - even

    for i in range(Q):
        if P_arr[i] % 2 == 0:
            print(even, odd)
        else:
            print(odd, even)
