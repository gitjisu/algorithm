import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    check = 'okay'
    for i in range(len(arr)-1):
        if arr[i].isdigit():
            stack.append(arr[i])
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if arr[i] == '+':
                    result = num1 + num2
                    stack.append(result)
                elif arr[i] == '*':
                    result = num1 * num2
                    stack.append(result)
                elif arr[i] == '-':
                    result = num1 - num2
                    stack.append(result)
                elif arr[i] == '/':
                    result = num1 // num2
                    stack.append(result)
            except: # 꺼낼 숫자가 없음
                check = 'error'

    if check == 'okay' and len(stack) == 1:
        print(f'#{tc} {stack.pop()}')
    elif check == 'error' or len(stack) > 1: # 스택에 숫자가 한개 이상 남아있으면
        print(f'#{tc} error')