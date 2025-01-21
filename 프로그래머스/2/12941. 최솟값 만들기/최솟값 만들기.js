function solution(A,B){
    // 오름차순 정렬
    const answer = []
    const a = A.sort((a,b) => a-b)
    // 내림차순 정렬
    const b = B.sort((a,b) => b-a)
    
    for (i=0; i<a.length; i++) {
        answer.push(a[i] * b[i])
    }
    
    return answer.reduce((a,b) => a+b)


}