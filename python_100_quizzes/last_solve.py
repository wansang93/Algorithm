def solution(n,l):
    result = 0
    mylist = [0 for i in range(n)]
    while l:
        for i in range(len(mylist)):
            if mylist[i] == 0 and l:
                mylist[i] = l.pop(0)
        mylist = list(map(lambda x: x-1, mylist))
        result += 1
    result += max(mylist)

    return result


배달원 = 3
배달시간 = [1,2,1,3,3,3]

print(solution(배달원,배달시간))
# 출력값 = 5