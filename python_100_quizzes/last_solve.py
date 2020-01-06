# 풀이86-1

def solution(point, dish):
    table = point.copy()
    dish -= 1
    result = 0
    is_OK = True
    while is_OK == True:
        overidx = 0
        for idx in range(len(table)):
            idx -= overidx
            result += 1
            if table[idx] == min(table):  # 테이블에서 가장 작은 값이면 먹어야된다.
                if dish == idx:  # 먹는 값이 내가 찾는거면
                    is_OK = False
                    result -= 1
                    break  # 브레이크
                else:  # 찾는게 아니면
                    table.pop(idx)  # 먹는다
                    overidx += 1  # 먹었으니 한칸씩 밀린다. 그러므로 idx에서 하나를 빼기위해 만들었다.
                    if idx < dish:  # 마찬가지로 먹으면 한칸씩 밀린다. dish값도 밀리기 때문에 1을 빼준다.
                        dish -= 1
    return result

# 풀이86-2

def solution2(point, dish):
#배열 순서는 0부터 시작, 입력은 1부터시작이기 때문에 -1 해준다.
    dish -=1
    answer = 0
    point = point.copy()
#오름차순으로 정렬
    s = sorted(point)
    while True:
# point 제일 앞의 점수를 추출하여  p에 넣어 놓는다. 즉, 앞에 도착한 접시의 점수!
# pop과 append를 활용해 회전하도록 구현할 예정 !
        p = point.pop(0)

        #현재 s[0]은 point 배열을 에서 가장 작은 값을 가지고 있음!
        #현재 가장 낮은 점수를 가지고 있는 접시가 앞에 도착했다면 먹도록 할것!
        if s[0]==p:
        #앞에 도착한 접시가 선택한 접시라면 먹고 반복문 종료
            if dish == 0:
                break
            #선택한 접시 움직임.          
            dish-=1
            #한 접시를 먹었음으로 하나 줄어듬
            s.pop(0)
        else:
            #접시위 초밥을 먹을 수 있는 조건이 충족되지 않아 그대로 둔다
            # pop했던것을 다시 append.
            point.append(p)
            #접시의 움직임 만약 선택한 접시가 앞에 도착했다면 맨뒤로 보내고,
            #그렇지 않다면 한칸 당긴다.
            dish = len(point)-1 if dish==0 else dish-1
            # 반복 한번당 접시 한번 지나감을 나타냄.
        answer+=1
    return answer


point = [5,2,3,1,2,5]
dish = 1
print('솔루션1', solution(point, dish))
print('솔루션2', solution2(point, dish))