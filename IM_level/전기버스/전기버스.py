import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    #one_charge: 이동가능한거리/ goal_stop: 종점 /charge_cnt: 충전소개수
    one_charge, goal_stop, charge_cnt = map(int, input().split())
    #charge_num : 충전가능한 정류장 번호
    charge_num = list(map(int, input().split()))
    charge_lst = [0] * (goal_stop+1)

    for i in range(len(charge_num)):
        charge_lst[charge_num[i]] += 1

        print(charge_lst)

    now = 0
    end = one_charge
    cnt = 0
    while True:
        zero = 0
        for i in range(now+1, end+1):
            if charge_lst[i] == 1:
                now = i
            else:
                zero += 1

        if zero == one_charge:
            cnt = 0
            break

        cnt += 1
        end = now + one_charge

        if end >= goal_stop:
            break

    print(f'#{tc} {cnt}')


