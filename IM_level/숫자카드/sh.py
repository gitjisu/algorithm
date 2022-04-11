import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input()))

    count_box = [0] * 10

    for i in boxes:
        count_box[i] += 1

    result = 0
    for i in range(len(count_box)):
        if result <= count_box[i]:
            result = count_box[i]
            idx = i

    print(f'#{tc} {idx} {result}')