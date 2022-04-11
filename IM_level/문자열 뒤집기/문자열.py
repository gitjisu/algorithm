import sys
sys.stdin = open('새 텍스트 문서.txt')
T = int(input())
for tc in range(1, T+1):
    string = input()
    reversed_str = ''
    for i in string:
        reversed_str = i + reversed_str

    print(f'{reversed_str}')