function solution(n, words) {
    let people = 0
    let turn = 0
    
    
    let check = []
    let alreadyWord = []

    for (p = 0;  p < n; p++) {
        check.push([])
    }
    

    
    
    let i = 0
    //1번사람 2번사람 3번사람
    let who = 0
    while (i < words.length) {
        // 가장 먼저 탈락하는 번호 who +1
        // 자신의 차례 check[who].length + 1
        // 중복 없이 다 끝내서 끝!
        if (alreadyWord.length === words.length) {
            break
        }
        // 이미 말한거면 탈락!!
        if (alreadyWord.includes(words[i])) {
                     people = who + 1
                    turn = check[who].length+1
                    break
        } else {
            // alreadyWord.pop()의 마지막 단어랑, words[i]의 첫글자가 같지 않으면 탈락
            if (alreadyWord.length > 0) {
                // 마지막 문자
                const lastWord = alreadyWord[alreadyWord.length - 1]
                const firstWord = words[i].slice(0, 1)
                if (lastWord.slice(lastWord.length-1) != firstWord) {
                    
                    people = who + 1
                    turn = check[who].length+1
                    break
                }
            }

            check[who].push(words[i])
            alreadyWord.push(words[i])
        }
        
        i++
        who ++
        if (who % n == 0) {
            who = 0
        } 
    }
    
    return [people, turn]
    
}