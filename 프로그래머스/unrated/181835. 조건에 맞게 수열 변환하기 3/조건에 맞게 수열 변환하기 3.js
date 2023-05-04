function solution(arr, k) {
    let i = 0
    if (k % 2 === 0) {
        while (i < arr.length) {
            arr[i] += k
            i ++
        }
    } else {
        while (i < arr.length) {
            arr[i] = arr[i] * k
            i ++
        }
    }
    
    return arr
}