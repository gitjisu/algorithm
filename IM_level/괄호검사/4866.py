import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    lst = []
    for i in s:
        if i == '(' or i == '{':
            lst.append(i)
        elif i == ')':
            if len(lst) == 0:
                lst.append('2')
            elif lst[-1] == '(':
                lst.pop()
            else:
                break
        elif i == '}':
            if len(lst) == 0:
                lst.append('2')
                break
            elif lst[-1] == '{':
                lst.pop()
            else:
                break
    if lst:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')