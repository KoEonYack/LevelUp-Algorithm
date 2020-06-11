"""
    @ Baek 1302 베스트셀러
    @ Prob. https://www.acmicpc.net/problem/1302
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 06. 11.
    @ End day: 20. 06. 11.
"""

dic = {}
maxV = 1
for _ in range(int(input())):
    s = input()
    if s in dic:
        dic[s] += 1
        if maxV < dic[s]:
            maxV = dic[s]
    else:
        dic[s] = 1

res = []
for key in dic.keys():
    if dic[key] == maxV:
        res.append(key)

res.sort()
print(res[0])



"""
5
top
top
aa
aa
kimtop
>
top

"""