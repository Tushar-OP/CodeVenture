# cook your dish her

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        x, k = map(int, input().rstrip().split())

        cnt = 0
        i = 2
        while i*i <= x:
            while x % i == 0:
                x //= i
                cnt += 1
            i += 1

        if x > 1:
            cnt += 1

        if cnt >= k:
            print(1)
        else:
            print(0)
