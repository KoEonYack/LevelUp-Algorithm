"""
    @ Baek 10978 소수 찾기
    @ Prob. https://www.acmicpc.net/problem/10978
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 28
    @ End day: 20. 01. 28
"""

def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

ans = 0
N = int(input())
arr = list(map(int, input().split()))

for val in arr:
    if isPrime(val):
        ans += 1

print(ans)


"""
4
1 3 5 7
>
3
"""