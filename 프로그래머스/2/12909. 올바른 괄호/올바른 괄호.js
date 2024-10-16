function solution(s){
    const stack = []

    for (i = 0; i < s.length; i++) {
        if (s[i] == '(') {
            stack.push('(')
        } else {
            if (i==0) {
                return false
            } else {
                stack.pop()
            }
        }
    }
    return stack.length === 0 ? true : false
}