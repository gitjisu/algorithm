function solution(s) {
    let result = []
    
    let spaceIndex = []
    
    let sliceWord = s.split(' ')
    

    
    for (let i = 0; i < sliceWord.length; i++) {
        for (let j = 0; j < sliceWord[i].length; j++) {
            if (j%2) {
                result.push(sliceWord[i][j].split(' ').join('').toLowerCase())
            } else {
                result.push(sliceWord[i][j].split(' ').join('').toUpperCase())
            }
        }
    }
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ') {
            spaceIndex.push(i)
        }
    }
    
    for (let i = 0; i < spaceIndex.length; i ++) {
        result.splice(spaceIndex[i], 0, ' ')
    }
    return result.join('')

//     for (let i = 0; i < s.split(' ').join('').length; i++) {
//         if (i%2) {
//             result.push(s.split(' ').join('')[i].toLowerCase())
//         } else {
//             result.push(s.split(' ').join('')[i].toUpperCase())
//         }
//     }
    
//     for (let i = 0; i < spaceIndex.length; i ++) {
//         result.splice(spaceIndex[i], 0, ' ')
//     }
//     return result.join('')
}