"""
    @ Baek 2693 N번째 큰 수
    @ Prob. https://www.acmicpc.net/problem/2693
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 06.
    @ End day: 20. 03. 06.
"""

for _ in range(int(input())):
    arr = []
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])


"""
4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408
>
8
489
931
768
"""