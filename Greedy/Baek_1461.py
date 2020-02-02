"""
    @ 1461. 도서관
    @ Prob. https://www.acmicpc.net/problem/1461
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

for i in range(0, N, M):
    take_books = books[i:i+M]
    print(take_books)
    cul_sum = 0
    for j in range(0, len(take_books)-1):
        cul_sum += abs(take_books[j] - take_books[j+1])


"""
7 2
-37 2 -6 -39 -29 11 -28
>
131
"""