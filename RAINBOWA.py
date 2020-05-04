if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().rstrip().split()))
                
        compare_a = a[::-1]
        
        duplicate_removed = []
        
        for i in range(n):
            if a[i] not in duplicate_removed:
                duplicate_removed.append(a[i])
        
        check_rainbow = [1,2,3,4,5,6,7]
        flag = 0
        if max(a) < 8:
            if compare_a == a:
                if duplicate_removed == check_rainbow:
                    flag = 1
        
        
        if flag == 1:
            print('yes')
        else:
            print('no')
    
    
    