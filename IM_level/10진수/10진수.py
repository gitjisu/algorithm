import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(T):
    a = input()

    temp = ''
    for i in range(len(a)):
        temp += a[i]
        if len(temp) == 7:
            result = int(temp, 2)
            print(result, end=' ')
            temp = ''
    print()

