import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())

def brute_force(pattern, text):
    i = j = 0
    p = len(pattern)
    t = len(pattern)
    while j < p and i < t: #패턴의 인덱스와 전체 인덱스가 문자 전체 길이 보다 작은 동안만 반복
        if pattern[j] != text[i]:
            i -= j
            j = -1
        i += 1
        j +=
    return 1 if j == p else 0

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = brute_force(str1, str2)
print(f'#{tc} {result}')