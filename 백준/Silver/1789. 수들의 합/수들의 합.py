input = int(input())

sum = 0
current_num = 0
while True:
    if sum + current_num > input:
        print(current_num-1)
        break
    sum += current_num
    
    current_num += 1


