MOD = 1000000007


def cal_exp(base, exp):
    res = 1

    while exp > 0:
        if exp % 2 == 1:
            res = (res*base) % MOD

        base = (base * base) % MOD
        exp = exp // 2

    print(res % MOD)


base = int(input())

exp = int(input())

cal_exp(base, exp)
