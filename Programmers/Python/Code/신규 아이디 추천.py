import re

def solution(new_id):
    result = new_id.lower()
    result = re.sub('[^a-z0-9\\.\\-\\_]', '', result)
    result = re.sub('\\.+' ,'.', result)
    if result.startswith('.'):
        result = result[1:]
    if result.endswith('.'):
        result = result[:-1]
    if not result:
        result = 'a'
    if len(result) >= 16:
        result = result[:15]
        if result.endswith('.'):
            result = result[:-1]
    if len(result) <= 1:
        result += result[-1] * 2
    elif len(result) == 2:
        result += result[-1]

    return result
