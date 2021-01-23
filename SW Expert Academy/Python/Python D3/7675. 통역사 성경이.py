import sys
sys.stdin = open(r'C:/Users/wansang/Desktop/Gitrep/Algorithm/SW Expert Academy/Python/Python D3/input.txt', 'r')

# # 문제가 잘못 된듯
# # 다른사람 코드 정답
# # 기본 테스트 케이스가 아래처럼 나왔는데 정답 처리가 됬음
# #1 3 0
# #2 2
# for tc in range(int(input())):
#     N = int(input())
#     answer = []
#     sentence = input()

#     # 문장 구분하기
#     start = 0
#     for i in range(len(sentence)):
#         if sentence[i] in ('!', '?', '.'):
#             # 단어로 구분하기
#             cnt = 0
#             for word in sentence[start:i].split():
#                 # 이름인지 판별하기
#                 if (len(word) == 1 and word[0].isupper()) or (
#                         word[0].isupper() and word.isalpha() and word[1:].islower()):
#                     cnt += 1
#             start = i + 2

#             answer.append(cnt)

#     print(f'#{tc + 1}', *answer)


# 내 풀이 (문제 오류)로 인한 해결 방법
def is_name(word):
    return word[0].isupper() and word.isalpha() and word[1:].islower()
T = int(input())
for t in range(1, T+1):
    N = int(input())
    answer = []

    paragraph = ''
    count = 0
    while True:
        text = input()
        count += text.count('.')
        count += text.count('?')
        count += text.count('!')
        paragraph += text
        if count == N:
            break

    start = 0
    count = 0
    for word in paragraph.split(' '):
        if len(word) == 1 and word[0].isupper():
            count += 1
        elif word[-1] in ('!', '?', '.'):
            if is_name(word[:-1]):
                count += 1
            answer.append(count)
            count = 0
        else:
            if is_name(word[:-1]):
                count += 1

    print(f'#{t}', *answer)
