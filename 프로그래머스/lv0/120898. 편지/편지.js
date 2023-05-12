function solution(message) {
    let result = message.replaceAll(" ", 'x')
    return result.length * 2
}