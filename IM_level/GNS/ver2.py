import sys
sys.stdin = open('GNS_test_input.txt')

code = [[[0 for _ in range(128)] for _ in range(128)] for _ in range(128)]
code[ord('Z')][ord('R')][ord('O')] = 0
code[ord('O')][ord('N')][ord('E')] = 1
code[ord('T')][ord('W')][ord('O')] = 2
code[ord('T')][ord('H')][ord('R')] = 3
code[ord('F')][ord('O')][ord('R')] = 4
code[ord('F')][ord('I')][ord('V')] = 5
code[ord('S')][ord('I')][ord('X')] = 6
code[ord('S')][ord('V')][ord('N')] = 7
code[ord('E')][ord('G')][ord('T')] = 8
code[ord('N')][ord('I')][ord('N')] = 9

digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for tc in range(1, T + 1):
    temp = input()
    arr = list(map(str, input().split()))
    count = [0] * 10
    for i in range(len(arr)):
        count[code[ord(arr[i][0])][ord(arr[i][1])][ord(arr[i][2])]] += 1

    # 카인팅 갯수 만큼 출력
    print(f'#{tc}')
    for i in range(10):
        for j in range(count[i]):
            print(digit[i], end=' ')
    print()