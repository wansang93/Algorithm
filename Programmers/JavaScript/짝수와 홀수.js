// 풀이1
function solution(a, b) {
    var answer = 0;
    
    if(a<=b){
      for(let i = a ; i <=b ; i++ ){
        answer = answer + i
      }    
    }
    if(a>b){
        for(let i = b; i <=a ; i++){
            answer =answer+i
        }
    }
    return answer;
}

// 풀이2
function adder(a, b){
    var result = 0
    return (a+b)*(Math.abs(b-a)+1)/2;
}