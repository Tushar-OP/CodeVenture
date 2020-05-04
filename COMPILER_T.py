# cook your dish her
from sys import stdin
if __name__=='__main__':
    t = int(stdin.readline())
    
    for _ in range(t):
        string = stdin.readline()
        
        str_arr = list(map(str, string))
        
        count = 0
        res = 0
        
        for i in range(len(string)):
            if str_arr[i] == '>':
                count -= 1
            else:
                count += 1
                
            if count == 0:
                res = i+1
            elif count < 0:
                break
                  
        print(res)
            
        
