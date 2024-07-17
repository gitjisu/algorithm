import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
score = list(map(int, input_data[1:]))

high = max(score)
tempArr = 0

for i in range(n):
    tempArr += (score[i] / high * 100)

print(tempArr / n)
