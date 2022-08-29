import sys
sys.stdin = open('1945.txt')

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    # num_list = [2, 3, 5, 7, 11]
    # cnt = [0] * 5

    # for i in range(len(num_list)):
    #     while True:
    #         if num % num_list[i] == 0:
    #             num = num // num_list[i]
    #             cnt[i] += 1
    #         else:
    #             break

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while True:
        if num % 2 == 0:
            num = num // 2
            a += 1
        else:
            break
    while True:
        if num % 3 == 0:
            num = num // 3
            b += 1
        else:
            break
    while True:
        if num % 5 == 0:
            num = num // 5
            c += 1
        else:
            break
    while True:
        if num % 7 == 0:
            num = num // 7
            d += 1
        else:
            break

    while True:
        if num % 11 == 0:
            num = num // 11
            e += 1
        else:
            break


    print(f'#{tc} {a} {b} {c} {d} {e}')


