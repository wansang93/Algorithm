def solution(n, delivery):
    # a[0] = 'O', '?', 'X'
    a = ['?'] * n
    delivery = list(sorted(delivery, key=lambda x: x[2], reverse=True))
    for l in delivery:
        if l[2] == 1:
            a[l[0]-1] = 'O'
            a[l[1]-1] = 'O'
        else:
            if a[l[0]-1] == 'O':
                a[l[1]-1] = 'X'
            elif a[l[1]-1] == 'O':
                a[l[0]-1] = 'X'
    
    answer = ''.join(a)
    return answer

print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))  # "O?O?X?"
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))  # "O?O?XXO"
