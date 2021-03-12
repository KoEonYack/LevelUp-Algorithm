"""
    @ Baek 5893 17배
    @ Prob. https://www.acmicpc.net/problem/5893
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

inputBin = input()
inputBin = "0b" + inputBin
tenDigit = int(inputBin, 2) * 17
print(bin(tenDigit)[2:])

"""
10110111
>
110000100111
"""