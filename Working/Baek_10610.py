"""
    @ Baek 10610
    @ Prob. https://www.acmicpc.net/problem/10610
      Ref. https://lmcoa15.tistory.com/48
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 25.
    @ End day: 19. 12. 25.
"""


inputStr = input()
arr = list(map(int, list(inputStr)))
numOfZero = 0
if 0 not in arr:
    print("-1")
else:
    totalArrSum = sum(arr)
    if totalArrSum % 3 != 0:
        print("-1")
    else:
        arr.sort(reverse=True)
        for num in arr:
            print(num, end="")
        #for num in arr:
        #    if num == 0:
        #        numOfZero += 1
        #    else:
        #        print(num, end="")
        #print("0"*numOfZero)


"""
30
30

102
210
"""