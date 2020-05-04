# cook your dish her

if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        m, x, y = map(int, input().rstrip().split())
        
        cops_houses = list(map(int, input().rstrip().split()))
        cops_houses.sort(reverse = True)
        
        max_range = x*y
        
        unsafe_houses = [0]*101
        total_houses = 100
        
        for i in range(m):
            j = cops_houses[i]
            k = cops_houses[i]
            while((j <= (cops_houses[i] + max_range)) and (j <= 100)):
                unsafe_houses[j] = 1
                j += 1
                
            while((k >= (cops_houses[i] - max_range)) and (k >= 1)):
                unsafe_houses[k] = 1
                k -= 1
        
        safe = 0 
        for i in range(1, 101):
            if unsafe_houses[i] == 0:
                safe += 1
        
        print(safe)
            
            
            
    


    
    
    