from sys import stdin, stdout

def count_number_of_ones(a, n):
    even = 0
    odd = 0
    for i in range(n):
        if a[i]%2 == 0:
            even += 1
    
    odd = n - even
            
    return even, odd
    
if __name__=='__main__':
    t = int(input())
    
    for _ in range(t):
        n, q = map(int, stdin.readline().rstrip().split())
        
        a = [bin(i).count("1") for i in list(map(int, stdin.readline().rstrip().split()))]
    
        p_list = []
    
        for i in range(q):
            p = int(stdin.readline())
            p_list.append(bin(p).count("1"))
        
        even, odd = count_number_of_ones(a, n)
        
        for i in range(q):
            if p_list[i]%2 == 0:
                print(even, odd)
            else:
                print(odd, even)
