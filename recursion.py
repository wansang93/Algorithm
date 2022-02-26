# 1~5까지 출력하기
def increase(i, N):
    # 중간식
    if i < N:
        print(i, end="")
        # i 증가
        increase(i+1, N)
        # print(i, end="")
        return
    print()

increase(1, 6)  # 1부터 6전까지

# 5~1까지 출력하기
def decrease(i, N):
    # 중간식
    if i > N:
        print(i, end="")
        # i 감소
        decrease(i-1, N)
        # print(i, end="")
        return
    print()

decrease(5, 0)  # 5부터 0전까지
