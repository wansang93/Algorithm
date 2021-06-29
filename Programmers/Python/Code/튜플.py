def solution(s):
    answer = []
    string = sorted(s[2:-2].split('},{'), key=len)
    for st in string:
        for srt_num in st.split(','):
            num = int(srt_num)
            if num not in answer:
                answer.append(num)

    return answer
