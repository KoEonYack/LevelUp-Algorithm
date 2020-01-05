"""
    @ Baek 2941 크로아티아 알파벳
    @ Prob. https://www.acmicpc.net/problem/2941
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

chro_data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inputStr = input()
for chro_char in chro_data:
    inputStr = inputStr.replace(chro_char, '+')

print(len(inputStr))

"""
ljes=njak
>
6
"""