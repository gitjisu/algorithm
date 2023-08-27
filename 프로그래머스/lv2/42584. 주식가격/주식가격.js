function solution(prices) {
    let answer = new Array(prices.length).fill(0)
    for (let i = 0; i < prices.length; i++) {
        for (let j = i + 1; j < prices.length; j++) {
            if (prices[i] <= prices[j]) {
                answer[i] += 1
            } else {
                answer[i] += 1
                break
            }
        }
    }
    
    return answer
}