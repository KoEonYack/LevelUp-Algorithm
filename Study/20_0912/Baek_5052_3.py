from sys import stdin
input = stdin.readline


def solution():
    pre_num = data.pop(0)

    for val in data:
        if val.startswith(pre_num):
            return "NO"
        pre_num = val
    return "YES"


for i in range(int(input())):
    valid = True
    N = int(input())
    data = sorted([stdin.readline().strip() for _ in range(N)])
    print(solution())


"""
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
>
NO
YES

"""