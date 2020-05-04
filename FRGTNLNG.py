if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().rstrip().split())
        
        dict_forgotten_words = list(input().rstrip().split())
        
        phrases = []
        for i in range(k):
            phrase = list(input().rstrip().split())
            phrases.append(phrase)
        
        flag = 0
        res = []
        for i in range(n):
            flag = 0
            for j in range(k):
                if dict_forgotten_words[i] in phrases[j]:
                    flag = 1
                    break
            
            res.append('YES') if flag == 1 else res.append('NO')
            
        print(*res)
                    
            
    
    
    
    