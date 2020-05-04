try:
   T = int(input())
except:
   T = 0
 
for _ in range(T):
    N, K= map(int, input().rstrip().split())
    Dict_words_arr = list(map(str, input().rstrip().split()))
    phrases = []
   
    for i in range(K):
       phrase = list(map(str,input().rstrip().split()))
       phrases.append(phrase)
 
    Flag = 0
    res = []
    for i in range(N):
        Flag = 0
        for j in range(K):
            if Dict_words_arr[i] in phrases[j]:
                Flag = 1
                break
        if Flag == 1:
             res.append("YES")
        else:
             res.append("NO")
    
    print(*res)
 



