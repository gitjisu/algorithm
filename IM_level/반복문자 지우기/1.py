import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1,T+1):
    s = input()
    l = len(s)
    stack = [] # A
    for i in range(l): # 0 1 2 3 4
        if not stack or stack[-1] != s[i]:
            stack.append(s[i])
        elif stack and stack[-1] == s[i]:
            stack.pop()
    print(f'#{tc} {len(stack)}')