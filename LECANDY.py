if __name__ == "__main__":
    try:
        T = int(input())
    except:
        T = 0
    for t in range(T):
        n, c = map(int, input().rstrip().split())
        arr = list(map(int, input().split()))
        
        if(sum(arr) <= c):
            print('Yes')
        else:
            print('No')