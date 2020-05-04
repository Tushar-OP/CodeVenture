if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        lst = list(map(int, input().rstrip().split()))
        
        lst_1 = []
        
        for i in range(n):
            if lst[i] == 1:
                lst_1.append(i)
                
        flag = False
        for i in range(len(lst_1)-1):
            if (lst_1[i+1] - lst_1[i]) < 6:
                flag = True
                break
        
        if flag:
            print('NO')
        else:
            print('YES')