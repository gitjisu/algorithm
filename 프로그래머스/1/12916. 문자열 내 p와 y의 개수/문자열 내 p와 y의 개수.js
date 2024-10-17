function solution(s){
    cnt_p = 0
    cnt_y = 0
    for (i=0; i<s.length; i++) {
        if (s[i] == 'p' | s[i] == 'P') {
            cnt_p += 1
        } else if (s[i] == 'y' | s[i] == 'Y') {
            cnt_y += 1
        }
    }
    
    return cnt_p == cnt_y ? true : false
}