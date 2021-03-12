"""
    @ 백준 16673 고려대학교에는 공식 와인이 있다
    @ https://www.acmicpc.net/problem/16673
    @ End Day : 2020. 03. 09.
"""

# 와인을 모은 년수
# 수빈이의 고려대 애착 정도
# 수빈이의 구매중독 정도
C, K, P = map(int, input().split())
res = 0
for i in range(1, C+1):
    res += K * i + P * i * i
print(res)

"""
3 1 1
>
20
--------------
5 28 27
>
1905
"""
