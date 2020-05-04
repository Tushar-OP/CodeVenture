if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        w = list(map(int, input().rstrip().split()))
        
        res = sum(w) - (len(w)*min(w))
        
        print(res)