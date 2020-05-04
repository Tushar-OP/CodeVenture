# cook your dish her

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        if n == 1:
            print(1)
            print(1, 1)
        else:
            print(n//2)
            if n % 2:
                print(3, 1, 2, n)
                for i in range(3, n, 2):
                    print(2, i, i+1)
            else:
                for i in range(1, n, 2):
                    print(2, i, i+1)
