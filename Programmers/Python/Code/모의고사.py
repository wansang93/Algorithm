# 풀이
def solution(answers):   
    answer = []
    solved = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0, 0, 0]
    
    for idx, value in enumerate(answers):
        for person in range(len(solved)):
            if value == solved[person][idx%len(solved[person])]:
                score[person] += 1
            
    for idx, value in enumerate(score):
        if value == max(score):
            answer.append((idx+1))
                        
    return answer

# 다른사람 풀이
def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

