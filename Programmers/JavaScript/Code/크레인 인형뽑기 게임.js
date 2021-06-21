function solution(board, moves) {
    var answer = 0;
    var stack = [];

    for (var i = 0; i < moves.length; i++) {
        var x = moves[i] - 1;
        for (var j = 0; j < board.length; j++) {
            if (board[j][x] != 0) {
                if (stack[stack.length - 1] === board[j][x]) {
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(board[j][x]);
                }
                board[j][x] = 0;
                break;
            }
        }
    }
    return answer;
}

// test case

// board = [
//   [0, 0, 0, 0, 0],
//   [0, 0, 1, 0, 3],
//   [0, 2, 5, 0, 1],
//   [4, 2, 4, 4, 2],
//   [3, 5, 1, 3, 1],
// ];
// moves = [1, 5, 3, 5, 1, 2, 1, 4];

// solution(board, moves);
