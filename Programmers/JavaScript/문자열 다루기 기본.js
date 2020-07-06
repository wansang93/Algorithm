    function solution(s) {
        if (!(s.length === 4 || s.length === 6)){
            return false
        }
        for (var i in s) {
            if (isNaN(s)){
                return false
            }
        }
        return true
    }