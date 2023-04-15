const solution = (c1, p1, c2,p2) => {
    
        c1 = c1 * p2
        c2 = c2 * p1
        c = c1 + c2
        p = p1 * p2

        
        let leastCommonMultiple = 1
        
        for (let i = 1; i <= c; i++) {
            if (c%i === 0 && p%i ===0) {
                leastCommonMultiple = i
            }
        }
        
        return [c/leastCommonMultiple, p/leastCommonMultiple]
}