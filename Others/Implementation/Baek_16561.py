"""
    @ Baek 16561. 3의 배수
    @ Prob. https://www.acmicpc.net/problem/16561
     Ref.
    @ Algo: 완전탐색
    @ Start day: 20. 07. 14.
    @ End day: 20. 07. 14.
"""

N = int(input())
ans = 0
for i in range(1, (N+1)//3):
    for j in range(1, (N+1)//3):
        cul =  i * 3 + j * 3
        # print("DEBUG", N, cul)
        if (N - cul) % 3 == 0 and N - cul > 0:
            ans += 1

print(ans)


"""
9
>
1
-----
12
>
3
"""