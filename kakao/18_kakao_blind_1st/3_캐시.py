"""
    @ 18 kako blind: 캐시
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/17680
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 06.
    @ End day: 20. 05. 06.
"""

from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0

    if cacheSize != 0:
        for city in cities:
            city = city.lower()
            if city in cache:
                cache.remove(city)
                cache.appendleft(city)
                time += 1
            elif city not in cache:
                if len(cache) >= cacheSize:
                    cache.pop()
                    cache.appendleft(city)
                    time += 5
                else:
                    cache.appendleft(city)
                    time += 5
    else:
        time += len(cities) * 5

    return time


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju"," Pangyo", "Seoul", "NewYork", "LA"]
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))