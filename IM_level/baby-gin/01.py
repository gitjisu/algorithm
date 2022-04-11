import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input()))
    count_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in arr:
        count_lst[i] += 1

    a = 0
    b = 0
    for j in range(len(count_lst)):
        if count_lst[j] >= 3:
            a += 1
            count_lst[j] -= 3
            if count_lst[j] >= 3:
                a += 1


        if count_lst[j] >= 1 and count_lst[j+1] >= 1 and count_lst[j+2] >= 1:
            b += 1
            count_lst[j] -= 1
            count_lst[j+1] -= 1
            count_lst[j+2] -= 1
            if count_lst[j] >= 1 and count_lst[j + 1] >= 1 and count_lst[j + 2] >= 1:
                b += 1



    if a + b == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')




