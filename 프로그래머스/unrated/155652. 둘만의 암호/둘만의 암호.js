function solution(s, skip, index) {
    const eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    let result = ''
    
    let word = s.split('')
    
    let skipWord = skip.split('')
    
    skipWord.map((i) => {
        if (eng.includes(i)) {
            eng.splice(eng.indexOf(i), 1)
        }
    })
    
    let i = 0
    let startWordIndex = eng.findIndex((item) => item === word[i])
    let nowWordIndex = startWordIndex
    let possibleWord = []
    

    while (result.length < s.length) {
        if (eng[nowWordIndex] === eng.at(-1) ) {
            nowWordIndex = -1
        }
        if (possibleWord.length === index) {
            result += possibleWord.at(-1)
            possibleWord = []
            i += 1
            startWordIndex = eng.findIndex((item) => item === word[i])
            nowWordIndex = startWordIndex
        } else {
            possibleWord.push(eng[nowWordIndex + 1])
            nowWordIndex += 1
        }
        
    }
    
    return result    
 }