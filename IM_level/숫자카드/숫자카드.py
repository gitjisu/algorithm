import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))

    box = [0] * 10  # 리스트생성

    for i in a:
        box[i] += 1 # 리스트에 집어 넣기
    print(box)

    max_num = 0  # 가장 많은 카드의 숫자
    max_card = box[0]  # 제일 많이 중복되는 카드 장 수
    for i in range(len(box)):
        if box[i] >= max_card:  # 박스의 i 번째가 max_card 보다 크면
            max_card = box[i]  # 값 바꾸기
            max_num = i

    print(f'#{tc} {max_num} {max_card}')







