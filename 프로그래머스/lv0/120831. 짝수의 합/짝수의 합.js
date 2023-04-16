function solution(n) {
    let temp = 0
    for (let i = 0; i <= n; i ++) {
        i % 2 ? temp += 0 : temp += i
    }
    
    return temp
}