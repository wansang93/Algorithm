T = int(input())
for t in range(1, T+1):
    matrix = []
    max_string_size = 1

    for i in range(5):
        temp = [c for c in input()]
        matrix.append(temp)
        if max_string_size < len(temp):
            max_string_size = len(temp)

    answer = ''
    for y in range(max_string_size):
        for x in range(len(matrix)):
            if len(matrix[x]) > y:
                answer += matrix[x][y]

    print(f'#{t} {answer}')
