import sys
sys.stdin = open('sample_input.txt')
T = int(input())
#k =  한번에 이동할 수 있는 거리
#n 목적지까지 정류장 갯수
#m 충전기 갯수 1 3 5 7 9

for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split())) # 1 3 5 7 9
    total = 0
    idx = 0
    gaze = k
    for i in range(1, n+1):
        gaze -= 1
        if i + gaze > charge[0]:
            idx += 1
        elif i + gaze > charge[idx]:
            id
        elif i + gaze == charge[idx]:
            gaze = 3
            idx += 1
            total += 1
        elif i + gaze < charge[idx]:
            print(f'#{tc} 0')
            break


