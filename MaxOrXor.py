from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())

    ele = list(map(int, stdin.readline().rstrip().split()))
    lucky_no =[]
    test = []
    ele.sort(reverse = True)
    for i in range(n):
        for j in range(n - 1):
            if ele[i] == ele[j + 1]:
                pass
            else:
                xor = ele[j] ^ ele[j + 1]
                lucky_no.append(xor)
    
    print(max(lucky_no))
        
      
   