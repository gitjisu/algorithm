import sys
sys.stdin = open('GNS_test_input.txt')
sys.stdout = open('GNS_output.txt', 'w')
digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for tc in range(1,T+1):
    c, n = input().split()
    arr = input().split()
    count = [0] * 10
    for i in arr:
        if i == digit[0] : count[0] += 1
        elif i == digit[1] : count[1] += 1
        elif i == digit[2] : count[2] += 1
        elif i == digit[3] : count[3] += 1
        elif i == digit[4] : count[4] += 1
        elif i == digit[5] : count[5] += 1
        elif i == digit[6] : count[6] += 1
        elif i == digit[7] : count[7] += 1
        elif i == digit[8] : count[8] += 1
        elif i == digit[9] : count[9] += 1

    print(f'#{tc}')
    for i in range(10):
        for j in range(count[i]):
            print(digit[i], end=' ')
