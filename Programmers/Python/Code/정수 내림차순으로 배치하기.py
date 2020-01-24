# 풀이1
def solution(n):
    answer = int("".join(sorted(str(n),reverse=True)))
    return answer

# 풀이2
def solution2(n):
    answer = int(''.join(reversed(sorted(str(n)))))
    return answer