def solution(cacheSize, cities):
    time = 0
    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)

    return time


# 다른 사람 풀이: collections 의 deque 를 이용하는 방법
import collections

def solution2(cacheSize, cities):
    time = 0
    cache = collections.deque(maxlen=cacheSize)

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5

    return time