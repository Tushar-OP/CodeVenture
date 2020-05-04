# cook your dish here
try:
    T = int(input())
except:
    T = 0
    
for t in range(T):
    N = int(input())
    N_inp = int(input())                  
    N_arr = list(map(int, str(N_inp)))
    c = N_arr.count(1)

    res = c * (c + 1)/ 2
    print(int(res))