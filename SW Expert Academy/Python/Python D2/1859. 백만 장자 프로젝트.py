# 풀이 시도1: 실패(런타임 오류)
T = int(input())
for i in range(T):
    N = int(input())
    mylist = list(map(int, input().split(' ')))
    answer = 0  # 정답
    cur = 0  # 리스트 커서의 위치

    while cur <= N-1:  # 커서가 마지막때까지 반복한다.
        now_max = max(mylist[cur:])  # 커서부터 시작한 리스트에서 가장 큰값을 찾는다.
        temp = cur + mylist[cur:].index(now_max)  # 가장 큰값으로 임시커서로 바꾼다.
        if cur != temp:  # 임시커서와 커서의 위치가 같지않으면(임시커서와 현재커서의 위치가 같으면 패스)
            for j in range(cur, temp):  # 커서 전까지 숫자를 커서값에서 뺀 각각의 값을 더한다.
                answer += now_max - mylist[j]
        cur = temp + 1  # 커서를 임시커서 다음칸으로 옮긴다.

    print('#{} {}'.format(i+1, answer))



# 풀이 시도2: 실패(런타임 오류)
T = int(input())
for i in range(T):
    N = int(input())
    mylist = list(map(int, input().split(' ')))
    answer = 0
    cur = 0  # 커서 위치

    while cur <= N-1:  # 커서가 마지막때까지 반복한다.
        now_max = max(mylist[cur:])  # 커서부터 시작한 리스트에서 가장 큰값을 찾는다.
        temp = cur + mylist[cur:].index(now_max)  # 가장 큰값으로 임시커서로 바꾼다.
        if cur != temp:  # 임시커서와 커서의 위치가 같지않으면
            while cur < temp:
                answer += now_max - mylist[cur]
                cur += 1
        cur += 1  # 커서를 임시커서 다음칸으로 옮긴다.

    print('#{} {}'.format(i+1, answer))



# 풀이 시도3: 
T = int(input())
for i in range(T):
    N = int(input())
    mylist = list(map(int, input().split(' ')))[::-1]  # 뒤에서부터 탐색
    answer = 0
    now_max = mylist[0]  # 현재 가장 큰 값

    for j in range(1, N):
        if now_max > mylist[j]:
            answer += now_max - mylist[j]
        else:
            now_max = mylist[j]

    print('#{} {}'.format(i+1, answer))