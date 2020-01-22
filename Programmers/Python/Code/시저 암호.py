# 풀이1
def solution(s, n):
    n = n % 26
    answer = ''
    for i in s:
        if i.islower():  # 소문자 범위
            if chr(ord(i)+n).islower() == 0:
                new = ord(i)+n-26
                answer += chr(new)
            else:
                answer += chr(ord(i) + n)
        elif i.isupper():  # 대문자 범위
            if chr(ord(i)+n).isupper() == 0:
                new = ord(i)+n-26
                answer += chr(new)
            else:
                answer += chr(ord(i) + n)
        else:
            answer += i
    return answer

# 풀이2
def solution2(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr(ord('A')+((ord(i) - ord('A') + n) % 26))
        elif i.islower():
            answer += chr(ord('a')+((ord(i) - ord('a') + n) % 26))
        else:
            answer += i
    return answer
