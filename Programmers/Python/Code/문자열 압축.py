def compress(string, length):
    newstr = ''  # 압축을 해줄 문자열
    count = 1
    next_s = ''
    for i in range(0, (len(string)//length - 1)*length, length):
        temp = string[i:i+length]
        next_s = string[i+length:i+length+length]
        if temp == next_s:  # 이전꺼와 다음께 같으면 카운트 업
            count += 1
        else:  # 다르면 카운트 종료
            if count > 1:  # 카운트가 1보다 크면
                newstr += str(count)  # 숫자를 넣어주고
                count = 1  # 카운트 초기화
            newstr += temp  # 글자 삽입

    # 반복문이 다 돌고나면 마지막 글자
    if count == 1:
        newstr += next_s
    else:
        newstr += next_s
        newstr += str(count)
    
    # 나머지 넣어주기
    if not (len(string) % length) == 0:
        newstr += string[-(len(string) % length):]
    return len(newstr)

def solution(s):
    answer = len(s)
    # if len(s) < 3:  # 글자 길이가 3보다 작으면 압축 필요가 없다.
    #     return answer
    # if len(s) == 3:  # 글자 길이가 3이면 3개가 같을 때만 압축효과가 있다.
    #     if s[0] == s[1] and s[1] == s[2]:
    #         return 2
    for i in range(1, len(s)//2 + 1):  # 글자 길이가 4 이상일 때 i값으로 압축한 것과 현재 값 비교
        answer = min(answer, compress(s, i))
    return answer
