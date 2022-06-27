def solution(n, words):
    answer = [0, 0]

    text = set([words[0]])
    before = words[0][-1]
    for i, word in enumerate(words[1:]):
        if word[0] != before or word in text:
            answer[0] = (i+1) % n + 1
            answer[1] = (i+1) // n + 1
            break
        before = word[-1]
        text.add(word)

    return answer

data1 = 3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
data2 = 5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
data3 = 2, ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(*data1))
print(solution(*data2))
print(solution(*data3))
