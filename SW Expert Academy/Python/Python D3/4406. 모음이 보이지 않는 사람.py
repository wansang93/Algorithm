# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 길이가 50이하이고 알파벳 소문자만으로 이루어진 단어가 주어진다.
# 이 단어에 모음이 아닌 문자(자음)이 적어도 하나는 들어있다는 것이 보장된다.

# [출력]
# 테스트 케이스 T에 대한 결과는 “#T ”을 찍고, 각 테스트 케이스마다 주어진 단어를 당신이 어떻게 인식하는지를 출력한다.

T = int(input())
for t in range(1, T+1):
    alphabets = input()
    consonants = ['a', 'e', 'i', 'o', 'u']

    answer = ''
    for c in alphabets:
        if not c in consonants:
            answer += c

    print(f'#{t} {answer}')