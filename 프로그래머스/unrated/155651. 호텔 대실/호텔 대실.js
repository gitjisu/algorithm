function solution(book_time) {
    // 정렬
    const sortedTime = book_time.sort()
    
    let usingRoom = []
    
    for (let time of sortedTime) {
        const [[startH, startM], [endH, endM]] = time.map(t => t.split(':'))
        
       const START_MINUTES = Number(startH) * 60 + Number(startM)
       
       const END_MINUTES = Number(endH) * 60 + Number(endM) + 10
       
       const index = usingRoom.findIndex(room => room <= START_MINUTES)
       
       if (index === -1) {
           usingRoom.push(END_MINUTES)
       } else {
           usingRoom[index] = END_MINUTES
       }
    }
    
    return usingRoom.length
    
}