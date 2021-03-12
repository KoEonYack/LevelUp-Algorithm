'''
    @ Baek 11720
    @ Prob. https://www.acmicpc.net/problem/11720
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
'''

N = int(input())
inputStr = input()
arr = list(inputStr)
arr = [int (i) for i in arr]
print(sum(arr))


"""
5
54321
>
15
"""