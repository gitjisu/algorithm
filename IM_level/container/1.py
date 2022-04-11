import sys
sys.stdin = open('1.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) #n컨테이너수 m트럭수
    w = sorted(list(map(int, input().split()))) # 각 컨테이너별 무게
    t = sorted(list(map(int, input().split()))) # 트럭 적재용량

    result = 0
    while w and t:
        truck = t.pop()
        while w:
            container = w.pop()
            if truck >= container:
                result += container
                break
    print(f'#{tc} {result}')
    