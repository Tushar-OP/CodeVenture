if __name__ == "__main__":
    N = int(input())
    res = []
    for _ in range(N):

        lst = list(map(str, input().rstrip().split()))
        

        if lst[0] == 'insert':
            res.insert(int(lst[1]), int(lst[2]))
        
        elif lst[0] == 'print':
            print(res)
        
        elif lst[0] == 'remove':
            res.remove(int(lst[1]))

        elif lst[0] == 'append':
            res.append(int(lst[1]))
        
        elif lst[0] == 'sort':
            res.sort()

        elif lst[0] == 'pop':
            res.pop()

        elif lst[0] == 'reverse':
            res.reverse()


