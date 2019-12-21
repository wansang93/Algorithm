a = ([1, 2],
     [2, 4])
b = ([1, 0],
     [0, 3])
    
# ([1,6], [2,12])

def solution(a, b):
    c = []
    if len(a) == len(b[0]):
        for i in range(len(a)):
            c.append([0]*len(b[0]))
        for i in range(len(c)):
            for j in range(len(c[i])):
                for k in range(len(a[i])):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    else:
        return -1

print(solution(a, b))