"""
    @ Baek 3181. 줄임말 만들기
    @ Prob. https://www.acmicpc.net/problem/3181
      Ref.
    @ Algo: String
    @ Start day: 20. 10. 31
    @ End day:  20. 10. 31
"""


arr = list(map(str, input().split()))
store = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
print(arr[0][0].upper(), end="")
print("".join(s[0] for s in arr[1:] if s not in store).upper())


"""
micro soft
>
MS
--------
biti ali i ne biti
>
BNB
"""