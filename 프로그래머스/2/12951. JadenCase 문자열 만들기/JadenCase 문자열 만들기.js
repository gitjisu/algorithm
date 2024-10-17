function solution(s) {
    
    let arr = s.split(' ').map(item => item.toLowerCase())
    
    
    arr.map((el, index) => {
        if (el == '') {
            return
        } else {
            if (isNaN(el[0])) {
               arr[index] = el[0].toUpperCase() + el.slice(1)
            } 
        }
    })
    
    return arr.join(' ')

}