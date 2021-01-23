function solution(answers) {

    let answer = [0, 0, 0];

    const a1 = [1, 2, 3, 4, 5];
    const a2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    var who = [];

    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === a1[i % a1.length]) answer[0]++;
        if (answers[i] === a2[i % a2.length]) answer[1]++;
        if (answers[i] === a3[i % a3.length]) answer[2]++;
    }

    var max = Math.max(answer[0], answer[1], answer[2])
    if (answer[0] === max) { who.push(1) };
    if (answer[1] === max) { who.push(2) };
    if (answer[2] === max) { who.push(3) };

    return who;
}


// 다른 사람 풀이
function solution(answers) {

    let answer = [];

    const a1 = [1, 2, 3, 4, 5];
    const a2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    let a1c = answers.filter((a, i) => a === a1[i % a1.length]).length;
    let a2c = answers.filter((a, i) => a === a2[i % a2.length]).length;
    let a3c = answers.filter((a, i) => a === a3[i % a3.length]).length;
    var max = Math.max(a1c, a2c, a3c);

    if (a1c === max) { answer.push(1) };
    if (a2c === max) { answer.push(2) };
    if (a3c === max) { answer.push(3) };

    return answer;
}
