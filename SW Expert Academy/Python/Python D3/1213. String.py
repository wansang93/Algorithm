for t in range(1, 11):
    T = int(input())
    find = input()
    string = input()

    answer = string.count(find)
    print(f'#{t} {answer}')