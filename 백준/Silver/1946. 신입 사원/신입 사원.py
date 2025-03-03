import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    # 각 지원자의 (서류심사 순위, 면접시험 순위)
    candidates = [list(map(int, input().split())) for _ in range(n)]
    
    # 서류심사 순위 기준으로 정렬
    candidates.sort(key=lambda x: x[0])
    
    cnt = 1
    best_interview = candidates[0][1]
    
    # 서류심사 순위가 낮은 순서대로 진행하므로,
    # 면접시험 순위가 지금까지의 최고(즉, 가장 낮은 숫자) 순위보다 작으면 선발
    for i in range(1, n):
        if candidates[i][1] < best_interview:
            cnt += 1
            best_interview = candidates[i][1]
    
    print(cnt)
