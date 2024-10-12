def solution(n):

    remain = 0
    result = 1
    while True:
        remain = n % result   
        if remain == 1 :
            break
        else :
            result += 1
    
            
    return result
            