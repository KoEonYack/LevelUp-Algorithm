"""
    @ Baek 5354 J박스
    @ Prob. https://www.acmicpc.net/problem/5354
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

for i in range(int(input())):
    num = int(input())
    print("#" * (num))
    for i in range(num-2):
        print("#" + "J" * (num - 2) + "#")
    print("#" * (num) + "\n")

"""
4
3
5
4
3
>
###
#J#
###

#####
#JJJ#
#JJJ#
#JJJ#
#####

####
#JJ#
#JJ#
####
"""