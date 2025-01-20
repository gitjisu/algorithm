function solution(name, yearning, photo) {
    const answer = []
    const matching = {}
    
    for (let i = 0; i < name.length; i++) {
        matching[name[i]] = yearning[i]
    }
    
    for (let i = 0; i < photo.length; i++) {
        let temp = 0
        for (let j = 0; j < photo[i].length; j++) {
            
             if (matching[photo[i][j]]) {
                temp += matching[photo[i][j]]
            }
        }
        answer.push(temp)
        
    }
    
    return answer
    
    
}