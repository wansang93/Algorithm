# 풀이1
def solution(jobs):
    answer = 0
    now = 0
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])
    while jobs:
        for i, job in enumerate(jobs):
            if job[0] <= now:
                now += job[1]
                answer += now - job[0]
                jobs.pop(i)
                break
        else:
            now += 1

    return answer // length


# 풀이2
import heapq


def solution(jobs):
    heap = []
    answer = 0
    length = len(jobs)
    now = 0

    while jobs or heap:
        for job in jobs[:]:
            if job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
                jobs.remove(job)
        if heap:
            processing = heapq.heappop(heap)
            now += processing[0]
            answer += now - processing[1]
        else:
            now += 1

    return answer // length

data = [[5, 3], [3, 9], [5, 6], [5, 100]]	
print(solution(data))

# 1. jobs를 뒤에 값으로 정렬(우선순위로 정렬)한다.
# 2. jobs가 없어질 때 까지 탐색한다.
    # 3. jobs를 탐색한다.
        # 3-1. 만약 jobs 안의 첫번째 값이 현재시간보다 작은 값으면:
            # 4. 해당 job을 실행한다(로직 수행).
                # 로직1) 현재시간 갱신
                # 로직2) answer 갱신
                # 로직3) jobs의 해당 job 삭제
                # 로직4) 2로 돌아가기
    # 3-1. jobs를 다 탐색했는데 현재시간보다 다 값이 작으면:
        # 현재시간 ++ 을 해준다.
