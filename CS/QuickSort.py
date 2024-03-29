def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr)//2]
  lesser_arr, equal_err, greater_arr = [], [], []
  for num in arr:
    if num < pivot:
      lesser_arr.append(num)
    elif num > pivot:
      greater_arr.append(num)
    else:
      equal_err.append(num)
  return quick_sort(lesser_arr) + equal_err + quick_sort(greater_arr)

  