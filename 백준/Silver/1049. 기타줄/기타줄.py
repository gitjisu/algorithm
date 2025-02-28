import sys

n, m = map(int, input().split())


result = 999999
pacakgas = []
singles = []

for _ in range(m) :
    pacakgePrice, singlePrice = map(int, input().split())
    pacakgas.append(pacakgePrice)
    singles.append(singlePrice)

min_pacakge = min(pacakgas)
min_single = min(singles)


#  패키지로만 구매하는 경우
def case1Func() :
    if (n%6 == 0) :
        return n//6 * min_pacakge
    else :
        return (n//6 + 1) * min_pacakge

case1 = case1Func()
        

#  낱개로만 구매하는 경우
case2 = n * min_single

#  패키지와 낱개를 섞어서 구매하는 경우
case3 = (n//6) * min_pacakge + (n%6) * min_single


result = min(case1, case2, case3)
print(result)

        

