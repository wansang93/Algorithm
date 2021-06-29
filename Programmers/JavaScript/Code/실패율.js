function solution(N, stages) {
    var result = {};
    var total = stages.length
    // stages(1~N)를 탐색하면서
    for (var stage = 1; stage < N+1; stage++) {
        // 현재 스테이지에 총원이 0이 아니면
        if (total != 0) {
            // 현재 스테이지에 사람이 몇명인지 확인
            let count = stages.filter(e => stage === e).length;
            // 실패율 구하기
            result[stage] = count / total
            // 총원 빼기
            total -= count
        }
        // 총원 0명에 아무도 못깼으면
        else {
            result[stage] = 0
        }
    }
    // console.log(result)

    // 
    let sortobj = [];
    for (let number in result) {
        sortobj.push([number, result[number]]);
    }
    sortobj.sort((a, b) => b[1] - a[1]);


    return sortobj.map(a => parseInt(a[0]));
}

var N = 5
var stages = [2,1,2,4,2,4,3,3]

console.log(solution(N, stages));
