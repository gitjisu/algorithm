import sys
sys.stdin = open('sample_input.txt')

# bubble sort 사용하기
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

T = int(input())
for tc in range(1, T+1):
    num_cnt = int(input())
    num = list(map(int, input().split()))
    bubble_sort(num)
    print(f'#{tc} {num[-1] - num[0]}')



    # min_value = num[0]
    # max_value = num[0]
    # for i in range(len(num)):
    #     if num[i] > max_value:
    #         max_value = num[i]
    # for j in range(len(num)):
    #     if num[j] < min_value:
    #         min_value = num[j]
    # print(f'#{tc} {max_value - min_value}')


# def bubble_sort(arr):
#     for i in range(len(arr))-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


