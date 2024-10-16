function solution(s) {
    const temp = s.split(' ')
    let max = Math.max(...temp)
    let min = Math.min(...temp)

    return `${min} ${max}`
}