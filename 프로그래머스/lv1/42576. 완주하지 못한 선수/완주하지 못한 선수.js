
function solution(participant, completion) {
    participant.sort();
    completion.sort(); 
    // console.log(participant)
    for(let i = 0; i < participant.length; i++){
        // console.log(participant[i], completion[i])
        if(participant[i] !== completion[i]){
            return participant[i];
        }
    }
}