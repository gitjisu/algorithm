# import sys, pprint
# sys.stdin = open("회문.txt")
# def is_palindrome(string):
#     result = ''
#     for s in string:
#         result = s + result
#     return True if result == string else False
#
# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     mat = [list(input()) for _ in range(n)]     # 2차원 배열 형태로 입력을 받고
#     alpha, beta = [], []                        # 1차원 배열로 변형시켜준다
#     for x in range(n):                          # alpha는 입력 상태 그대로 1차원 배열로 바꾸고
#         r, r2 = '', ''                          # beta는 전치행렬 형태로 바꾼다
#         for y in range(n):
#             r += mat[x][y]
#             r2 += mat[y][x]
#         alpha.append(r)
#         beta.append(r2)
#
#     result = ''                                 # 결과값 출력할 변수 지정
#     b = False                                   # 찾으면 바로 탈출할 수 있게 탈출변수를 지정해줬다.
#     for i in range(n):
#         for j in range(n-m+1): # alpha와 beta의 각 행에대해 m의 길이의 palindrome이 있는지 검사
#             if is_palindrome(alpha[i][j:j + m]):
#                 result = alpha[i][j:j + m]
#                 b = True  # 있다면 탈출변수 True로 바꾸고 break
#                 break
#             if is_palindrome(beta[i][j:j + m]):
#                 result = beta[i][j:j + m]
#                 b = True
#                 break
#         if b:  # 있다면 그 밖의 for문도 바로 탈출
#             break
#
#     print(f"#{tc} {result}")\
#
#
import random
num =
for i in range(1, 7):
    num.append(random.sample(range(1, 46), 1))
print(num)