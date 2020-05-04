if __name__ == "__main__":
    try:
        T = int(input())
    except:
        T = 0
    salary = []
    res = []
    for t in range(T):
        n = int(input())
        w = list(map(int, input().rstrip().split()))
        w.sort()
        salary.append(list(w))
        f = 0
        
        for i in salary:
            x = i[0]
            for j in i:
                print(j)


                
    
