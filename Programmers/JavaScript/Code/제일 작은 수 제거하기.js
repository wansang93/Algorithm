function solution(arr) {
    if (arr.length === 1) {
        return [-1]
    }

    var minNum = arr[0];
    var idx = 0;

    for (var i = 1; i < arr.length; i++) {
        if (minNum > arr[i]){
            minNum = arr[i];
            idx = i;
        }
    }
    arr.splice(idx, 1);
    
    return arr;
}

// 풀이2
function solution2(arr) {
    if (arr.length === 1 ) {
        return [-1]
    }
    const minValue = Math.min.apply(null, arr)
    const index = arr.findIndex(value => value === minValue)
    arr.splice(index, 1)

    return arr;
}