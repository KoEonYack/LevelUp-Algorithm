"""
    백준 2164번 카드2
    Prob https://www.acmicpc.net/problem/2164
    End Day : 2020. 1. 1
"""

from collections import deque

card_num = int(input())
card_deque = deque([i for i in range(1, card_num + 1)])

while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[0])

"""
6

> 4
"""

