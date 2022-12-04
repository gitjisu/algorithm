def counting_sort(arr):
    count = dict()
    sorted_arr = list()
    
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in sorted(count.keys()):
        for _ in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr