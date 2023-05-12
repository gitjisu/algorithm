function solution(numbers, n) {
    let result = 0
    for (i in numbers) {
        if (result + numbers[i] > n) {
            result += numbers[i]
            return result
        } else {
            result += numbers[i]
        }
    }
    
}