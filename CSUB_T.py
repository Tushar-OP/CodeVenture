if __name__ == '__main__':
    t = int(input())
     
    for _ in range(t):
        
        n = int(input())
        try:
            inp = int(input())
        except:
            inp = 0
        
        
        inp_array = list(map(int, str(inp)))
        
        no_ones = inp_array.count(1)
        
        count = (no_ones * (no_ones+1))//2
        
        print(count)