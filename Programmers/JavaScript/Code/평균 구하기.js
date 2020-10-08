function solution(arr) {
    var sum = 0;
    for(var i = 0; i < arr.length; i++) {
        sum += arr[i]
    }
    return sum / arr.length;
}

// 풀이2
function solution2(arr) {
    return arr.reduce((a, b) => a + b) / arr.length;
}