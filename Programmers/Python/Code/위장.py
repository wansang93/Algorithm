def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        clothes_dict[key] = clothes_dict.get(key, 0) + 1

    for value in clothes_dict.values():
        answer *= value+1
    
    answer -= 1
    return answer


data = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(data))
