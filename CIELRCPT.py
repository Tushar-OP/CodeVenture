# cook your dish her

if __name__ == '__main__':
    t = int(input())

    p_list = []

    menu = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

    for _ in range(t):
        p_list.append(int(input()))

    for z in range(t):

        p = p_list[z]
        count = 0

        i = 0
        while(i < 12) and(p != 0):
            while p >= menu[i]:
                p -= menu[i]
                count += 1

            i += 1

        print(count)
