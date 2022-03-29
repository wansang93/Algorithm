# 8, 13, 23 실패
def dfs(ap_sc, li_sc, n, k, lilst, aplst):
    global answer, max_dif
    if k == 11:
        if n > 0:
            lilst[k-1] = n
        diff = li_sc - ap_sc
        if max_dif <= diff:
            max_dif = diff
            answer = lilst

        return

    ap_get = aplst[k]
    # ap를 10-k점수를 넘어갈 경우
    if n > ap_get:
        new_lst = lilst[:]
        new_lst[k] = ap_get+1
        dfs(ap_sc, li_sc+10-k, n-ap_get-1, k+1, new_lst, aplst)
    # ap를 10-k점수를 안 넘어갈 경우
    if aplst[k]:
        ap_sc += 10-k
    dfs(ap_sc, li_sc, n, k+1, lilst, aplst)

def solution(n, info):
    global answer, max_dif
    answer = [-1]
    max_dif = 0
    dfs(0, 0, n, 0, [0]*11, info)
    return answer



data1 = 5
data11 = [2,1,1,1,0,0,0,0,0,0,0]
data2 = 1
data22 = [1,0,0,0,0,0,0,0,0,0,0]
data3 = 9
data33 = [0,0,1,2,0,1,1,1,1,1,1]
data4 = 10
data44 = [0,0,0,0,0,0,0,0,3,4,3]

print(solution(data1, data11))  # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(data2, data22))  # [-1]
print(solution(data3, data33))  # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(data4, data44))  # [1,1,1,1,1,1,1,1,0,0,2]
