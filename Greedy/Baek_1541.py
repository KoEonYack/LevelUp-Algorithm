"""
    @ 1541. 잃어버린 괄호
    @ Prob. https://www.acmicpc.net/problem/1541
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 01.
    @ End day: 20. 02. 01.
"""

equation = input()
split_minus = equation.split("-")
flag = False
if len(split_minus) == 1:
    flag = True
cul_sum = 0

for i in range(0, len(split_minus)):
    split_plus = split_minus[i].split("+")
    #print(split_plus)
    for num in split_plus:
        cul_sum += int(num)
        print(num)

if flag is False:
    #print(split_minus, cul_sum)
    print(split_minus)
    print(int(split_minus[0])*2 - cul_sum)
else:
    print(cul_sum)


"""
55-50+40
>
-35

55-50+40-30+20
>
85

0+10+20
>
30
0-1-2


3+2+322-22
>

"""