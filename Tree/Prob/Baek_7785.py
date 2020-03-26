"""
    @ Baek 7785. 회사에 있는 사람
    @ Prob. https://www.acmicpc.net/problem/7785
     Ref.
    @ Algo: Tree
    @ Start day: 20. 03. 26.
    @ End day: 20. 03 26.
"""

import sys

data = dict()
for i in range(int(input())):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        data[name] = True
    else:
        del data[name]

print("\n".join(sorted(data.keys(), reverse=True)))

"""
4
Baha enter
Askar enter
Baha leave
Artem enter
>
Askar
Artem
"""




