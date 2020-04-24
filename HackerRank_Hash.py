if __name__ == "__main__":
    n = int(input())
    t = tuple(map(int, input().rstrip().split()))

    print(hash(t))  #hash() is a builtin function, returns hash of only immutable obj.
