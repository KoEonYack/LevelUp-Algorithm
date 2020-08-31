"""
    @ Baek 11047. 동전0
    @ Prob. https://www.acmicpc.net/problem/11047
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 04. 20.
    @ End day: 20. 04. 20.
"""



N, Target = map(int, input().split())
moneys = []
for _ in range(N):
    moneys.append(int(input()))
moneys.reverse()
ans = 0

for money in moneys:
    while Target // money > 0:
        num_coins, Target = divmod(Target, money)
        ans += num_coins

print(ans)
    
    
    

"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
>
6

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
>
12

"""