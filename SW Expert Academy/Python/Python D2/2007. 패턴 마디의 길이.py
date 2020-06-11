# 문제 조건이 불분명해서
# 패턴이 여러개인 경우 패턴의 길이가 최소인 경우를 패턴 이라고 가정하고 풀었습니다.
T = int(input())
for t in range(1, T+1):
    string = input()
    pattern = ''

    for i in range(1,11):
        if string[0:i] == string[i:2*i]:
            pattern = string[0:i]
            break

    print(f'#{t} {len(pattern)}')