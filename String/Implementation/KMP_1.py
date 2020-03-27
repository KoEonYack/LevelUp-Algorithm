"""
    Ref. https://deque.tistory.com/78
    2020. 03. 27
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

print(count)
for c in result:
    print(c)

