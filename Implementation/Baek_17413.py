"""
    @ Baek 17413
    @ Prob. https://www.acmicpc.net/problem/17413
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

inputStr = input()
stack = []

for ch in inputStr:
    if ch == "<" or ch == " ":
        if ch == "<":
            stack.append("9")
        print("".join(stack)[::-1], end="")
        stack.clear()
        if ch == " ":
            print(" ", end="")
    elif ch == ">":
        stack.append(ch)
        print("".join(stack)[::], end="")
        stack.clear()
    else:
        stack.append(ch)

if stack:
    print("".join(stack)[::-1], end="")


"""
baekjoon online judge
>
noojkeab enilno egduj


<open>tag<close>
>
<open>gat<close>


<ab cd>ef gh<ij kl>
>
<ab cd>fe hg<ij kl>
"""