# 풀이1
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    sum_bridge = 0
    while True:  # 대기트럭이 없고 다리상태가 빌때 종료
        answer += 1  # 1초씩 증가시킴
        sum_bridge -= bridge[0]  # 다리 상태 체크
        bridge.pop(0)  # 다리 1초후 상황인 0번째를 뺌
        
        if truck_weights != [] and sum_bridge + truck_weights[0] <= weight:
        # 대기 트럭이 비면 실행 안하고 다리 상태에 추가될 트럭이 무게보다 작으면 실행
            sum_bridge += truck_weights[0]
            bridge.append(truck_weights.pop(0))  # 대기 트럭 명단에 빼서 다리에 추가
        else:
            bridge.append(0)  # 다리에 빈것 추가

        if truck_weights == [] and bridge == [0] * bridge_length:
        # 대기 트럭이 비고 다리 상태가 비면 종료
            break
    return answer

# 풀이2
def solution2(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    sum_bridge = 0
    sum_waiting = sum(truck_weights)
    while sum_waiting or sum_bridge:
        answer += 1
        sum_bridge -= bridge.pop(0)

        if truck_weights == []:
            pass    
        elif sum_bridge + truck_weights[0] <= weight:
            sum_bridge += truck_weights[0]
            sum_waiting -= truck_weights[0]
            bridge.append(truck_weights.pop(0))
        elif sum_bridge + truck_weights[0] > weight:
            bridge.append(0)

    return answer

# 풀이3
def solution3(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    sum_bridge = 0
    while truck_weights != [] or sum_bridge:
        answer += 1
        sum_bridge -= bridge.pop(0)

        if truck_weights == []:
            pass    
        elif sum_bridge + truck_weights[0] <= weight:
            sum_bridge += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return answer