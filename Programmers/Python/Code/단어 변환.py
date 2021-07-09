from collections import defaultdict
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    words = [begin] + words[:]
    l = len(words)
    bl = len(begin)
    graph = defaultdict(list)
    for i in range(l-1):
        first_word = words[i]
        for j in range(i+1, l):
            second_word = words[j]
            # 비교1
            cnt = 0
            for i in range(bl):
                if first_word[i] != second_word[i]:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1:
                    graph[first_word].append(second_word)
                    graph[second_word].append(first_word)

    print(graph)
    # 1. 탐색이 불가능하면 0을 리턴한다.

    # 2. 단어들을 탐색하며 그래프화 한다.
        # 첫번째 단어(출발)(hit+words)들 반복
            # 두번째 단어(도착)(words)들 반복
                # 비교(1글자만 다르면?)
                    # 그래프에 연결(첫단어 -> 두번째 단어)
                    # 그래프에 연결(두번째 단어 -> 첫단어)

    # 3. 그래프 완성시 그래프를 탐색한다.(최단 경로 알고리즘 사용)






    return answer


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
