import sys
sys.stdin = open('test.txt')

move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def set_case(x, y):
    global min_len, cnt
    if min_len <= cnt:
        return

    for i, j in move_list:
        dx = x + i
        dy = y + j
        try:
            if arr[x][y] == 1 or arr[dx][dy] == 1:
                if arr[dx][dy] == 0:
                    arr[dx][dy] = 'x'
                    cnt += 1
                    set_case(dx, dy)
        except:
            pass

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    min_len = 9999999999999999
    set_case(0, 0)

    print(cnt)