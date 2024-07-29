def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    answer = 0
    for i in range(row_begin-1, row_end):
        xor = 0
        for v in data[i]:
            xor += v % (i+1)
        answer ^= xor
    return answer
