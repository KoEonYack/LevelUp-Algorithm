"""
    @ Baek 16916 부분 문자열
    @ Prob. https://www.acmicpc.net/problem/16916
      Ref. 
            https://www.youtube.com/watch?v=GTJr8OvyEVQ
    @ Algo: KMP
    @ Start day: 20. 03. 27
    @ End day: 20. 03. 27
"""

# S = input()
# P = input()

S = "baekjoon"
P = "aek"

pi = [0] * len(P)
count = 0
j = 0

for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j
    

textLen = len(S)
patternLen = len(P)
j = 0
for i in range(textLen):
    while j > 0 and S[i] != P[j]:
        j = pi[j-1]
        
    if S[i] == P[j]:
        if j == patternLen - 1:
            count += 1
            j = pi[j]
        else:
            j += 1

print(1 if count > 0 else 0)



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