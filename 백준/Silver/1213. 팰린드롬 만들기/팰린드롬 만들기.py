import sys

input_str = input().strip()  # 입력 받기

dictions = {}

# 각 문자의 빈도수 계산
for i in input_str:
    if i in dictions:
        dictions[i] += 1
    else:
        dictions[i] = 1

# 알파벳 순으로 정렬
sortedDict = dict(sorted(dictions.items()))

countSingle = 0  # 홀수 개수의 문자를 찾기 위한 변수
middle_char = ''  # 회문 중간에 들어갈 문자

# 홀수 개수의 문자가 2개 이상이면 불가능
for key, value in sortedDict.items():
    if value % 2 == 1:
        countSingle += 1
        middle_char = key  # 홀수 개수인 문자는 한 번만 중앙에 배치

if countSingle > 1:
    print("I'm Sorry Hansoo")
else:
    # 결과 리스트를 생성
    result = [''] * len(input_str)
    mid = len(result) // 2  # 중앙 인덱스

    # 홀수 개수인 문자가 있을 경우 중앙에 배치
    if middle_char:
        result[mid] = middle_char
        sortedDict[middle_char] -= 1  # 중앙에 배치한 문자는 횟수를 1 감소

    # 양쪽 끝에 문자 배치
    left = 0
    right = len(result) - 1
    for key, value in sortedDict.items():
        # 각 문자를 등장 횟수의 절반만큼 양쪽 끝에 배치
        for _ in range(value // 2):
            result[left] = key
            result[right] = key
            left += 1
            right -= 1

    # 결과 출력
    print(''.join(result))
