function solution(numbers, hand) {
    const position = [
        [ 3, 1, 'center'],
        [ 0, 0, 'L'],
        [ 0, 1, 'center'],
        [ 0, 2, 'R'],
        [ 1, 0, 'L'],
        [ 1, 1, 'center'],
        [ 1, 2, 'R'],
        [ 2, 0, 'L'],
        [ 2, 1, 'center'],
        [ 2, 2, 'R'],
    ]
    
    let result = ''
    let prevRightPosition = [3, 2, 'R']
    let prevLeftPosition = [3, 0, 'L']

    
    for (let i = 0; i < numbers.length; i ++) {
        // if (i === 0) {
        //     result += position[numbers[i]][2]
        //     if (position[numbers[i]][2] === 'L') {
        //         prevLeftPosition = position[numbers[i]]
        //     } else if (position[numbers[i]][2] === 'R') {
        //         prevRightPosition = position[numbers[i]]
        //     } else {
        //         if (hand === 'right') {
        //             prevRightPosition = position[numbers[i]]
        //         } else if (hand === 'left') {
        //             prevLeftPosition = position[numbers[i]]
        //         }
        //     }
        // // }
        // else {
            if (position[numbers[i]][2] === 'center') {
                let moveCntLeft = 0
                let moveCntRight = 0
                if (!!prevRightPosition.length) {
                    moveCntRight += Math.abs(position[numbers[i]][0] - prevRightPosition[0])
                    moveCntRight += Math.abs(position[numbers[i]][1] - prevRightPosition[1])
                } 
                if (!!prevLeftPosition.length) {
                    moveCntLeft += Math.abs(position[numbers[i]][0] - prevLeftPosition[0])
                    moveCntLeft += Math.abs(position[numbers[i]][1] - prevLeftPosition[1])
                }
                
                if (moveCntLeft < moveCntRight) {
                    result += 'L'
                    prevLeftPosition = position[numbers[i]]
                } else if (moveCntLeft > moveCntRight) {
                    result += 'R'
                    prevRightPosition = position[numbers[i]] 
                } else if (moveCntLeft == moveCntRight) {
                    if (hand === 'left') {
                        result += 'L'
                        prevLeftPosition = position[numbers[i]]
                    } else if (hand === 'right') {
                        result += 'R'
                        prevRightPosition = position[numbers[i]]
                    }
                }
                
            }
            else if (position[numbers[i]][2] === 'L') {
                result += 'L'
                prevLeftPosition = position[numbers[i]]
            } else if (position[numbers[i]][2] === 'R') {
                result += 'R'
                prevRightPosition = position[numbers[i]]
            }
            
        }
    // }
    
    return result
}