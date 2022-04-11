import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
    cnt_dic = {}
    str1 = input()
    str2 = input()

    for i in str1:
        cnt_dic[i] = cnt_dic.get(i,0)

    for j in str2:
        try:
            cnt_dic[j] += 1
        except KeyError:
            pass

    ans = 0
    for v in cnt_dic.values():
        if v > ans:
            ans = v
    print(f'#{tc} {ans}')