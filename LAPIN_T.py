# cook your dish her

if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        string = input()
        
        str_len = len(string)
        middle = 0
        if str_len%2 == 0:
            middle = int(len(string)/2)
            first_half_string = string[:middle]
            second_half_string = string[middle:str_len]
        else:
            middle = (len(string)//2)
            first_half_string = string[:(middle)]
            second_half_string = string[(middle+1):str_len]
            
        flag = 0
        
        for i in range(middle):
            if first_half_string[i] in second_half_string:
                second_half_string = second_half_string.replace(str(first_half_string[i]), ' ', 1)
            else:
                flag = 1
                break
            
            
        if flag == 0:
            print('YES')
        else:
            print('NO')
            
            
    
    
                
            
    


    
    
    