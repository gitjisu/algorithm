import sys
sys.stdin = open('1.txt')

def win(a, b):       #  가위바위보
    if arr[a] == arr[b]:      #    같으면 앞에 있는ㅇ ㅐ가 이김
        return a
    if arr[a] == 3 and arr[b] == 1:  # 보 가위 = 가위
        return b
    if arr[a] == 1 and arr[b] == 3: # 가위 보 = 가위
        return a
    if arr[a] > arr[b]: #바위 > 가위 / 가위 > 보
        return a


def team(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        winner = win(arr[0], arr[1])
        if arr[0] == winner:
            return arr[0:1]
        else:
            return arr[1:]
    else:
        if len(arr) % 2 == 0 :
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]
        else:
            left = arr[:len(arr)//2+1]
            right = arr[len(arr)//2+1:]
        return team(team(left) + team(right))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    idx = [i for i in range(n)]
    result = team(idx)
    print(result[0]+1)