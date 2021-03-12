"""
    @ Baek 10173 니모를 찾아서
    @ Prob. https://www.acmicpc.net/problem/10173
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 23
    @ End day: 20. 01. 23
"""

while True:
    inputStr = str(input()).upper()
    if inputStr == "EOI":
        break
    else:
        if "NEMO" in inputStr:
            print("Found")
        else:
            print("Missing")

"""
Marlin names this last egg Nemo, a name that Coral liked.
While attempting to save nemo, Marlin meets Dory,
a good-hearted and optimistic regal blue tang with short-term memory loss. 
Upon leaving the East Australian Current,(888*%$^&%0928375)Marlin and Dory
NEMO leaves for school and Marlin watches NeMo swim away.
EOI
>
Found
Found
Missing
Missing
Found


Upon leaving the East Australian Current,(888*%$^&%0928375)Marlin and Dory
EOI
"""


