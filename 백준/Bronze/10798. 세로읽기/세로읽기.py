import sys
input = sys.stdin.read

# 입력 읽기
data = input().strip().split('\n')

# 각 줄의 문자열을 배열로 저장
arr = [line for line in data]

# 최대 문자열 길이 구하기
maxLen = max(len(line) for line in arr)

result = ''

# 세로로 읽기
for col in range(maxLen):
    for row in range(5):
        if col < len(arr[row]):
            result += arr[row][col]

print(result)
