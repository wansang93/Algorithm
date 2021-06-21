function solution(array, commands) {
    var answer = [];

    for (var i = 0; i < commands.length; i++) {
        temp = array.slice(commands[i][0]-1, commands[i][1]).sort((a, b) => a-b)
        answer.push(temp[commands[i][2]-1])
    }

    return answer;
}

solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])