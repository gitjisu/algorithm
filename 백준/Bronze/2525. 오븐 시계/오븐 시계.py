import sys

input_data = sys.stdin.read().strip().split('\n')

h, m = map(int, input_data[0].split())
cookingTime = int(input_data[1])

# 현재 시각을 분 단위로 변환
now_m = h * 60 + m

# 조리 시간을 더한 후의 시각 계산
end_m = now_m + cookingTime

# 24시간(1440분)을 넘어가는 경우 처리
if end_m >= 1440:
    end_m -= 1440

# 계산된 시각을 시와 분으로 변환하여 출력
hour = end_m // 60
minute = end_m % 60

print(hour, minute)
