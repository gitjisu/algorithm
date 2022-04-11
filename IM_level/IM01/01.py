import sys
sys.stdin = open('01.txt')
for tc in range(5):
    area = input() # 3
    student = list(map(int,input().split())) # 3 4 5
    chong, bu = list(map(int, input().split())) # 2 2
    total = 0
    for i in student: # [10 9 10 9 10]
        total += 1
        temp = i - chong
        if temp > 0:
            if temp <= bu:
                total += 1
            else:
                total += (temp//bu) + 1
    print(total)