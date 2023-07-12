function solution(skill, skill_trees) {
    
    function isPossible(i, split_skills) {
        // i = BACDE , split_skills = C, B, D
        let cnt = 0 //스킬 순서를 확인
        for (let str of i) {
            // b 3까지 스킬 순서만큼 반복
            // 스킬 트리 문자열이 i 번째의 스킬과 같은지 확인
            //cnt 수보다 skills 배열 인덱스가 더 클 경우 순서가 맞지 않는 것이므로 false 반환
            //위의 경우에서 반환되지 않을 경우 스킬 순서와 일치한 것이므로 true 반환
            for (let k = 0; k < split_skills.length; k ++) {
                if (str === split_skills[k]) {
                    if (cnt < k) {
                        return 1
                    }
                    cnt += 1
                }
            } 
        } return 0
    }
    
    let answer = 0
    const split_skills = skill.split('')
    
    for (let i of skill_trees) {
        if (!isPossible(i, split_skills)) {
            answer += 1
        }
    }
    
    return answer
}