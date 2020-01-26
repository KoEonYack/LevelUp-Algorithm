"""
    @ Baek 10808 알파벳 개수
    @ Prob. https://www.acmicpc.net/problem/10808
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""
# ord('a') - 97

inputStr = input()
arr = [0] * 26
for ch in inputStr:
    arr[ord(ch) - 97] += 1

for ch in arr:
    print(ch, end=" ")

"""
baekjoon
>
1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
"""
