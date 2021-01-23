function solution(participant, completion) {
    let answer = '';
    participant.sort();
    completion.sort();
    for (let i in participant) {
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }
}

// 다른 사람 풀이
function solution(participant, completion) {
    let answer = '';
    participant.sort();
    completion.sort();
    while (participant.length) {
        let pp = participant.pop()
        if (pp !== completion.pop()){
            return pp
        }
    }
}
