import sys
input = sys.stdin.read

# 입력 받기
input_data = input().strip().split()
arr = list(map(int, input_data))

# 중복된 값 찾기
count = [0] * 7  # 주사위 눈의 개수를 카운트하기 위한 배열

for num in arr:
    count[num] += 1

# money 계산
money = 0

if max(count) == 3:  # 모두 같은 경우
    money = 10000 + (arr[0] * 1000)
elif max(count) == 2:  # 두 개가 같은 경우
    for i in range(1, 7):
        if count[i] == 2:
            money = 1000 + (i * 100)
            break
else:  # 모두 다른 경우
    money = max(arr) * 100

print(money)
