# cook your dish her
if __name__ == '__main__':
    try:
        t = int(input())
    except:
        t = 0

    for _ in range(t):
        n = int(input())

        res = 0

        if n < 4:
            print(0)
        else:
            for i in range(1, n // 2):
                res += i
            print(res)
