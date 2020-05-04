if __name__ == "__main__":
    try:
        T = int(input())
    except:
        T = 0
    
    for t in range(T):
        x, y, k, n = map(int, input().rstrip().split()) 
        
        p_c_arr = []
        for i in range(n):
            p, c = map(int, input().rstrip().split())          
            p_c_arr.append([p,c])
            
        chef_can_buy_book = False

        
        for i in range(n):
            if (p_c_arr[i][1] <= k ):
                if(p_c_arr[i][0] + y >= x):
                    chef_can_buy_book = True
                    break
    
        if(chef_can_buy_book):
            print('LuckyChef')
        else:
            print('UnluckyChef')
