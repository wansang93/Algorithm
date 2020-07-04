function solution(n) {
    return '수박'.repeat(n/2) + ((n%2) ? '수' : '');
}

// 풀이2
function solution(n) {
    return "수박".repeat(n).slice(0, n);
}