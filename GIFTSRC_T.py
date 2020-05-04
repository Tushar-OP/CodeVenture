# cook your dish her
from sys import stdin
if __name__=='__main__':
    t = int(stdin.readline())
    
    for _ in range(t):
        n = int(stdin.readline())
        
        moves = stdin.readline()
        
        moves_list = list(map(str, moves))
        
        repeat = False
        
        final_cell = [0,0]
        
        x_axis = ['L', 'R']
        y_axis = ['U', 'D']
        
        prev_move = 0
        for i in range(n):
            repeat = False
            
            if (prev_move in x_axis and moves_list[i] in x_axis) or (prev_move in y_axis and moves_list[i] in y_axis):
                repeat = True
            
            if not repeat:
                if moves_list[i] == 'L':
                    final_cell[0] = final_cell[0] - 1
                elif moves_list[i] == 'R':
                    final_cell[0] = final_cell[0] + 1
                elif moves_list[i] == 'U':
                    final_cell[1] = final_cell[1] + 1
                elif moves_list[i] == 'D':
                    final_cell[1] = final_cell[1] - 1
            
            prev_move = moves_list[i]
            # print(prev_move)
        
        print(*final_cell)
                
            
                
        
                
            
    


    
    
    