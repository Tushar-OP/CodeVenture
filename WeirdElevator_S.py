
import math

def primeFactors(n):  
    prime_factors_lst = []
    while n % 2 == 0: 
        prime_factors_lst.append(2)
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2): 
      
        while n % i== 0: 
            prime_factors_lst.append(i)
            n = n / i 

    if n > 2: 
        prime_factors_lst.append(n)
    
    return prime_factors_lst

def main():
    T = int(input())
    for _ in range(T):
        res = []
        x, y, m = map(int, input().rstrip().split())

        common_gcd = math.gcd(x, y)

        prime_number_x = x / common_gcd
        prime_number_y = y /common_gcd

        x_res = primeFactors(prime_number_x)
        y_res = primeFactors(prime_number_y)

        for i in range(len(x_res)):
            res.append(x_res[i])

        for i in range(len(y_res)):
            res.append(y_res[i])
        
        for i in range(len(res)):
            f = 0
            if res[i] > m:
                f = 1
                break
            else:
                continue
        if(f == 0):
            print(len(res), common_gcd)
        else:
            print(-1)


        





if __name__ == "__main__":
    main()


 