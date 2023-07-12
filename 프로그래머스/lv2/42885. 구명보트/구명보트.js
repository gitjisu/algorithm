// 한번에 최대 2명 100키로까지

function solution(people, limit) {
    
    const array = people.sort((a, b) => a-b)

    let boat = 0
    let lightest = 0
    let heaviest = array.length - 1
    

    
    while (lightest < heaviest) {
        if (array[lightest] + array[heaviest] <= limit) {
            lightest += 1
            heaviest -= 1
        } else {
            heaviest -= 1
        }
        
        boat += 1
    }
    
    if (lightest == heaviest) {
        boat += 1
    }

    return boat
}