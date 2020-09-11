def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    answer = 0

    for i in range(A, B+1):
        str_i = str(i)
        k = i ** (1/2)
        if k != int(k):  # i값의 루트가 정수가 아니면 패스
            continue
        if is_palindrome(str_i) and is_palindrome(str(int(k))):
            answer += 1

    print(f'#{t} {answer}')