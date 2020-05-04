
# Contest Code:COOK116B
# Problem Code:GIFTSRC

from sys import stdin, stdout 
try:
    T = int(stdin.readline()) 
except:
    T = 0

for _ in range(T):
    n = int(stdin.readline())
    moves = list(map(str, stdin.readline().rstrip()))

    repeat = False
    x_axis = ['L', 'R']
    y_axis = ['U', 'D']
    prev_move = 0
    x = 0
    y = 0

    for i in range(n):
        repeat = False

        if(prev_move in x_axis and moves[i] in x_axis) or(prev_move in y_axis and moves[i] in y_axis):
            repeat = True
        
        if not repeat:
            if moves[i] == 'L':
                x -= 1
            elif moves[i] == 'R':
                x += 1
            elif moves[i] == 'U':
                y += 1
            elif moves[i] == 'D':
                y -= 1
        prev_move = moves[i]
    print(x, y)
            