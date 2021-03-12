"""
    @ Baek 11944 NN
    @ Prob. https://www.acmicpc.net/problem/11944
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""


N, M = map(str, input().split())
M = int(M)
result_str = N * int(N)
print(result_str[:M])


"""
20 16
>>
2020202020202020
"""