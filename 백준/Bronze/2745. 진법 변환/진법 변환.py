import sys


# 입력 받기
N, B = input().split()
B = int(B)  # 진법 B를 정수로 변환

# 알파벳 대문자를 숫자로 매핑하는 딕셔너리
alphabet = {
  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
  'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
  'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
  'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
  'Y': 34, 'Z': 35
}

result = 0

# 문자열을 역순으로 처리하며 각 자릿값을 계산
for i, char in enumerate(reversed(N)):
    if char.isdigit():
        value = int(char)  # 문자가 숫자일 경우
    else:
        value = alphabet[char]  # 문자가 알파벳일 경우
    
    result += value * (B ** i)

print(result)
