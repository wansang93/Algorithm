# a = input().split(' ')
# n, k = a


# def sol(n, k):
#     i = 0
#     #q에 n만큼의 숫자를 넣어준다
#     q = [i for i in range(1,n+1)]

#     while len(q) > 2:
#         if i > len(q)-1:
#             while i > len(q)-1:
#         #순환하다 i가 q의 길이보다 클 경우에 len(q)만큼 빼준다.
#         #[1,2,3,4,5,6] -> 1다음 4가 빠지고 그 다음은 4+3 = 7(index : 6)이 빠져야 하는데 
#         #i(현재 빠져야 할 index)가 len(q)보다 크므로 len(q)즉, 4를 빼준다. 
#         #이걸 마지막 2개가 남을 때 까지 반복함
#                 i -= len(q)
#         q.pop(i)
#         i += k
#         i -= 1
#     print(q)

# sol(int(n),int(k))

def solution(n, k):
    mylist = [i for i in range(1, n+1)]
    eating = []
    now = 0
    eating.append(mylist[now])
    while len(mylist)-len(eating) > 2:
        next_k = []
        while len(next_k) < k:
            if now >= len(mylist):  # 화살표가 초과했을 때, 0으로 돌아r감
                now = now % len(mylist)
            if mylist[now] in eating:  # 화살표가 먹은 것에 있으면 다음 것으로 바꿈
                now += 1
            else:  # 화살표가 가르키는게 먹을 것이면 다음 먹을 것에 추가
                next_k.append(mylist[now])
                now += 1
        eating.append(next_k[-1])

    return list(set(mylist)-set(eating))


n, k = map(int, input().split())
print(solution(n, k))
