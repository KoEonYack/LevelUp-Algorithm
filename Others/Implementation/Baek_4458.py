"""
    @ Baek 4458 첫 글자를 대문자로
    @ Prob. https://www.acmicpc.net/problem/4458
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

for _ in range(int(input())):
    inputStr = input()
    print(inputStr[0].upper() + inputStr[1:])


"""
5
powdered Toast Man
skeletor
Electra Woman and Dyna Girl
she-Ra Princess of Power
darth Vader
>
Powdered Toast Man
Skeletor
Electra Woman and Dyna Girl
She-Ra Princess of Power
Darth Vader
"""