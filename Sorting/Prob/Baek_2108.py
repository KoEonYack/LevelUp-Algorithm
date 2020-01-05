"""
    @ Baek 2108
    @ Prob. https://www.acmicpc.net/problem/2108
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 01. 04
    @ End day:  20. 01. 04
"""

"""
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
"""

from collections import Counter


def median():
    if N == 1: return arr[0]
    else: return (arr[N//2] if N%2 != 0 else round((arr[N//2] + arr[N//2-1]) / 2))


def frequency():
    mode_dict = Counter(arr)
    modes = mode_dict.most_common()
    if len(arr) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod

N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort()

print(round(sum(arr)/N))
print(arr[N//2])
print(frequency())
print(arr[-1] - arr[0])


"""
https://hwiyong.tistory.com/175


5
-1
-2
-3
-1
-2

>>
-2
-2
-1
2
"""