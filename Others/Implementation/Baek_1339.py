"""
    @ Baek 1339 단어 수학
    @ Prob. https://www.acmicpc.net/problem/1339
      Ref.
      Ref Prob.
    @ Algo: 시뮬레이션
    @ Start day: 20. 08. 10.
    @ End day: 20. 08. 10.
"""


alpha = [0] * 26
for _ in range(int(input())):
    ss = input()
    ss = ss[::-1]
    for i in range(len(ss)):
        alpha[ord(ss[i]) - ord('A')] += pow(10, i)

alpha.sort(reverse=True)
ans = 0
for i in range(9, 0, -1):
    ans += i * alpha[9-i]
print(ans)

"""
2
AAA
AAA
>
1998
----
2
GCF
ACDEB
>
99437
"""