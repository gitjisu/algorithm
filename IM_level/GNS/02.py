import sys
sys.stdin = open('GNS_test_input.txt')

new = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for tc in range(T):
    c, n = input().split()
    num = input().split()
    newsort = []

    for i in new:
        for j in num:
            if i == j:
                newsort += [i]

    print(c, newsort)