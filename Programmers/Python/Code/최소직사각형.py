def solution(sizes):
    x_max = 0
    y_max = 0
    for size in sizes:
        size.sort()
        x_max = max(x_max, size[0])
        y_max = max(y_max, size[1])

    return x_max * y_max
