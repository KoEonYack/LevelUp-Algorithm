"""
    @ 1874 스택 수열
    @ Prob. https://www.acmicpc.net/problem/1874
     Ref.
    @ Algo: Stack
    @ Start day: 20. 02. 16.
    @ End day: 20. 02. 16.
"""


N = int(input())
stack = [0]
currV = 0
cycle = 0
result = []
while cycle != N:
    target = int(input())
    cycle += 1
    if target > currV:
        while True:
            currV += 1
            stack.append(currV)
            #print("+")
            result.append("+")
            if target == currV:
                stack.pop()
                #print("-")
                result.append("-")
                break
    elif target == stack[-1]:
        stack.pop()
        result.append("-")
        #print("-")


if len(stack) > 1:
    print("NO")
else:
    for ch in result:
        print(ch)


"""
8
4
3
6
8
7
5
2
1
>
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
-------------------------
5
1
2
5
3
4
>
NO
"""