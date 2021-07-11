# 코드가 너무 난잡함
# DFS나 BFS로 풀면 더 좋았을 듯

def solution(places):
    answer = []
    N = 5
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for place in places:
        for row in range(N):
            for column in range(N):
                if place[row][column] == 'P':
                    for dir in direction:
                        nr = row + dir[0]
                        nc = column + dir[1]
                        # 구간 조사
                        if 0 <= nr < N and 0 <= nc < N:
                            # 사람 앉으면 브레이크
                            if place[nr][nc] == 'P':
                                break
                            # 자리가 O 이면
                            elif place[nr][nc] == 'O':
                                # 한번 더 조사
                                for dir2 in direction:
                                    nnr = nr + dir2[0]
                                    nnc = nc + dir2[1]
                                    # 구간 조사
                                    if 0 <= nnr < N and 0 <= nnc < N:
                                        # 기존이랑 겹치면 무시
                                        if nnr == row and nnc == column:
                                            continue
                                        # 사람 앉으면 브레이크
                                        if place[nnr][nnc] == 'P':
                                            break
                                else:
                                    continue
                                break
                    else:
                        continue
                    break
            else:
                continue
            break
        else:
            answer.append(1)
            continue
        answer.append(0)
            
    return answer
