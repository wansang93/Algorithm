def solution(record):
    result = []
    temp = []
    
    status = {}
    for info in record:
        texts = info.split()
        if texts[0] == 'Enter':
            status[texts[1]] = texts[2]
            temp.append((texts[1], 'Enter'))
        elif texts[0] == 'Leave':
            temp.append((texts[1], 'Leave'))
        elif texts[0] == 'Change':
            status[texts[1]] = texts[2]
    
    for t in temp:
        if t[1] == 'Enter':
            result.append(f'{status[t[0]]}님이 들어왔습니다.')
        elif t[1] == 'Leave':
            result.append(f'{status[t[0]]}님이 나갔습니다.')


    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))