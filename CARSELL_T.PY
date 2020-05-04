# cook your dish her

if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
    
        p = list(map(int, input().rstrip().split()))
        
        p.sort(reverse = True)
        
        profit = 0
        
        for i in range(n):
            if p[i] - i <= 0:
                break
            else:
                profit += (p[i] - i)
        
        print(profit%1000000007)
    
        
                
            
    


    
    
    