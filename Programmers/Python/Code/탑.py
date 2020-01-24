# 풀이1
def solution(heights):
    answer = []
    buildings = [0]
    for i in heights:
        buildings.append(i)
        if i >= max(buildings):
            answer.append(0)
        else:
            k = -2
            while True:
                if buildings[-1] < buildings[k]:
                    answer.append(len(buildings)+k)
                    
                    break
                k -= 1
                          
    return answer

# 풀이2
def solution2(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans

# 풀이3
def solution3(h):
    answer = [0] * len(h)
    while h:
        right = h.pop()
        for idx in range(len(h)-1,-1,-1):
            if h[idx] > right:
                answer[len(h)] = idx+1
                break
    return answer