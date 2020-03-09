"""
    @ 백준 11557 Yangjojang of The Year
    @ https://www.acmicpc.net/problem/11557
    @ End Day : 2020. 03. 09.
"""

max_C = ""
max_D = -1
for _ in range(int(input())):
    for i in range(int(input())):
        C, D = map(str, input().split())
        if int(D) > max_D:
            max_C = C
            max_D = int(D)

    print(max_C)
    max_D = -1


"""
2
3
Yonsei 10
Korea 10000000
Ewha 20
2
Yonsei 1
Korea 10000000
>
Korea
Korea

"""