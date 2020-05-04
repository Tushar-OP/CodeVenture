if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        
        m = list(map(int, input().rstrip().split()))
        
        count_wolverine = 0
        for i in range(n):
            m[i] = m[i] + k
        
        for i in range(n):
            if m[i]%7 == 0:
                count_wolverine += 1
                
        print(count_wolverine)
    
    
    
    