import sys


chess = [1, 1, 2, 2, 2, 8]

input_data = sys.stdin.read()
input = list(map(int, input_data.split()))


result = []

for i in range(len(input)):
  result.append(chess[i] - input[i])


print(' '.join(map(str, result)))