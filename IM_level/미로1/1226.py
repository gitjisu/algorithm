
import sys
sys.stdin = open('1.txt')

move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
def dfs(y, x):
    global result
    if map_list[y][x] == 3:
        result = 1
        return
    for i, j in move_list:
        d_y = y + i
        d_x = x + j
        if map_list[d_y][d_x] != 1 :
            map_list[y][x] = 1
            dfs(d_y, d_x)			
        
 
T = 10
for _ in range(T):
    t = int(input())
    N = 16
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    dfs(1,1)
    print(f'#{t} {result}')