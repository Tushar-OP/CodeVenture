try:
    t = int(input())
except:
    t = 0

for _ in range(t):
    x, y, k, n = map(int, input().rstrip().split())
    
    pc = []
    for i in range(n):
        p, c = map(int, input().rstrip().split())
        pc.append([p, c])
        
        
    pages_required = x-y
    can_buy = 0
    
    for i in range(n):
        if pc[i][1] <= k:
            if pc[i][0] >= pages_required:
                can_buy = 1
                break
            
    if can_buy == 1:
        print('LuckyChef')
    else:
        print('UnluckyChef')
            
            
            
            
            