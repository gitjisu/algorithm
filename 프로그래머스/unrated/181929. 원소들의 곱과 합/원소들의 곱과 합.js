function solution(num_list) {
    let timesResult = 1
    let plusResult = 0
    for (let i = 0; i < num_list.length; i ++) {
        timesResult = timesResult * num_list[i]
        plusResult += num_list[i]
    }
    
    return timesResult < plusResult * plusResult ? 1 : 0
}