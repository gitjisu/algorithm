import sys
sys.stdin = open('1.txt')

t = int(input())
for tc in range(1, t+1):
    arr = list(input().split())
    stack = []
    flag = 'okay'
    for i in range(len(arr)-1):
        if arr[i].isdigit():
            stack.append(arr[i])
        else:
            try:
                num1, num2 = int(stack.pop()), int(stack.pop())
                if arr[i] == '+':
                    tmp = num1 + num2
                    stack.append(tmp)
                elif arr[i] == '*':
                    tmp = num1 * num2
                    stack.append(tmp)
                elif arr[i] == '-':
                    tmp = num1 - num2
                    stack.append(tmp)
                elif arr[i] == '/':
                    tmp = num1 // num2
                    stack.append(tmp)
            except:
                flag = 'error'


    if len(stack) == 1 and flag == 'okay':
        print(f'{stack.pop()}')
    elif len(stack) != 1 or flag == 'error':
        print(f'error')
