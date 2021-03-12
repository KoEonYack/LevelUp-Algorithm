"""
    @ Baek 1316
    @ Prob. https://www.acmicpc.net/problem/1316
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

def groupCheck(words):
    a = []
    a.append(words[0])
    for i in range(1, len(words)):
        if words[i-1] == words[i]:
            pass
        else:
            if words[i] in a:
                return 0
            else:
                a.append(words[i])
    return 1

cnt = 0

for i in range(int(input())):
    words = input()
    cnt += groupCheck(words)

print(cnt)

"""
3
happy
new
year
>
3
"""