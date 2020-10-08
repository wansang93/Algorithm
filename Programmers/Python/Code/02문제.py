c0, c1 = 0, 0  # count 0, count 1

def is_right(arr, length, n):
    global c0, c1
    if length == 1:

        pass
    else:
        is_same = arr[0][0]
        for y in range(length):
            for x in range(length):
                if is_same != arr[y][x]:
                    break
            else:
                continue
            break

def solution(arr):
    is_right(arr, len(arr), len(arr))
    return [c0, c1]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
