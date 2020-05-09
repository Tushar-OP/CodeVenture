T = int(input())


for _ in range(T):
    N = int(input())
    X = list(map(int, input().rstrip().split()))
    R = 1
    Res_list = []
    

    for i in range(N-1):
        if abs(X[i] - X[i+1]) <= 2:
            R += 1
        else:
            Res_list.append(R)
            R = 1
    
    Res_list.append(R)
    print(min(Res_list), max(Res_list))
