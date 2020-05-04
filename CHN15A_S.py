if __name__ == "__main__":
    try:
        T = int(input())
    except:
        T = 0

    initial_char_of_N = []
    K_arr = []

    for t in range(T):
        N, K = map(int, input().rstrip().split())
        n = list(map(int, input().rstrip().split()))
        initial_char_of_N.append(n)
        K_arr.append(K)

    sum_with_k_final = []

    for i in range(len(initial_char_of_N)):

        sum_with_k_initial = []

        for j in range(len(initial_char_of_N[i])):
            s = 0
            s = initial_char_of_N[i][j] + K_arr[i]
            sum_with_k_initial.append(s)

        sum_with_k_final.append(sum_with_k_initial)

    for i in range(len(sum_with_k_final)):

        Wolverine_like_minions = 0

        for j in range(len(sum_with_k_final[i])):
            if sum_with_k_final[i][j] % 7 == 0:
                Wolverine_like_minions = Wolverine_like_minions + 1
                
        print(Wolverine_like_minions)
