"""
    백준 11866. 조세퍼스 문제 0 ??????
    Prob https://www.acmicpc.net/problem/11866
    End Day : 2020. 1. 1
"""


from collections import deque

N, K = map(int, input().split())
card_deque = deque([str(i) for i in range(1, N + 1)])
mid = K - 1
"""
print("<", end="")
while len(card_deque) > K-1:
    print(card_deque[K-1], end=", ")
    card_deque.remove(card_deque[K-1])
    card_deque.rotate(-(K-1))
"""
answer = []

for i in range(N):
    if len(card_deque) > mid:
        answer.append(card_deque[K - 1])
        #print(card_deque[K - 1], end=", ")
        card_deque.remove(card_deque[K - 1])
        card_deque.rotate(-(K - 1))
    elif len(card_deque) <= mid:
        mid = mid % len(card_deque)
        card_deque.rotate(-(mid - 1))
        #print(card_deque.pop(), end=", ")
        answer.append(card_deque.pop())
        mid += K - 1

#print(", ".join(card_deque), end="")
print("<", end="")
print(", ".join(answer), end="")
print(">")


"""
7 3
1 2 3 4 5 6 7
>
<3, 6, 2, 7, 5, 1, 4>
"""
