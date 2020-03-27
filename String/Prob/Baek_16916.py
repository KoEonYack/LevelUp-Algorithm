"""
    @ Baek 16916 부분 문자열
    @ Prob. https://www.acmicpc.net/problem/16916
      Ref.
    @ Algo: KMP
    @ Start day: 20. 03. 27
    @ End day: 20. 03. 27
"""

S = input()
P = input()
pi = [0 for i in range(len(P))]
result = []
count = 0

j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j

j = 0
patternLen = len(P)
textLen = len(S)
for i in range(textLen):
    while j > 0 and S[i] != P[j]:
        j = pi[j-1]
    if S[i] == P[j]:
        if j == patternLen - 1:
            result.append(i-patternLen + 2)
            count += 1
            j = pi[j]
        else:
            j += 1

if count > 0:
    print(1)
else:
    print(0)

"""
baekjoon
aek
>
1
-----------------
baekjoon
bak
>
0
"""