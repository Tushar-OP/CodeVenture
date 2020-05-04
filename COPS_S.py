try:
    T = int(input())
except:
    T = 0

for _ in range(T):
    m,x,y = map(int, input().rstrip().split())
    cops_houses = list(map(int, input().rstrip().split()))

    check_element = x * y
    arr_of_100_numbers = []

    for i in range(1, 102):
        arr_of_100_numbers.append(0)

    for i in range(m):
        right_direction_numbers = cops_houses[i] + check_element
        left_direction_numbers = cops_houses[i] - check_element

        if left_direction_numbers < 1:
            left_direction_numbers = 1
        if right_direction_numbers > 100:
            right_direction_numbers = 100

        for j in range(left_direction_numbers, right_direction_numbers+1):
            arr_of_100_numbers[j] = 1

    count_of_unsafe_house = arr_of_100_numbers.count(0) - 1
    print(count_of_unsafe_house)    
    

    

