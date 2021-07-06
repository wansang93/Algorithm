def solution(genres, plays):
    answer = []
    genre_total_play = {}
    index_info = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_total_play[genre] = genre_total_play.get(genre, 0) + play
        index_info[genre] = index_info.get(genre, []) + [(play, i)]

    for most in sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True):
        for each in sorted(index_info[most[0]], key=lambda x: x[0], reverse=True)[:2]:
            answer.append(each[1])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
