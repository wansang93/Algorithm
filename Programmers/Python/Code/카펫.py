def solution(brown, yellow):
    answer = []
    carpet = brown + yellow
    for horizontal in range(carpet, 2, -1):
        if carpet % horizontal == 0:
            vertical = carpet // horizontal
            if (horizontal-2) * (vertical-2) == yellow:
                return [horizontal, vertical]
        

def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            # (세로 길이 + 가로 길이) *2 + 4 = 브라운 갯수(브라운 둘레)
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]

data = 8
data2 = 1
print(solution(data, data2))
