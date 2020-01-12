import re


def solution(s):
    idx = re.split("[0-9]번: ",s)  # ['', '3,1 ', '4 ', '2,1,3 ', '2,1,3,4']
    idx = idx[1:]                  # ['3,1 ', '4 ', '2,1,3 ', '2,1,3,4']
    mylist = []
    for c in idx:
        mylist.append(list(map(int, c.replace(' ','').split(','))))

    print(mylist)

    result = []
    for l in mylist:
        for i in l:
            if i not in result:
                result.append(i)
    
    return result


i = '1번: 3,1 2번: 4 3번: 2,1,3 4번: 2,1,3,4'

print(solution(i))