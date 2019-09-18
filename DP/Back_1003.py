'''
    @ 백준 - DP
    @ Prob. https://www.acmicpc.net/problem/1003
    @ Ref.  https://dpdpwl.tistory.com/57
    @ Algo: Dynamic Programming
    @ Start day: 19. 09. 18
    @ End day: 19. 09. 18
'''

dp = [0] * 41
dp[1] = 1

N = int(input())

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]
    print(dp[i])

'''
while N:
    N = N - 1
    for i in range
'''

