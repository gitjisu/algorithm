import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
     num = int(input())
     string = str(num)
     print(f'#{tc} {string} {type}')