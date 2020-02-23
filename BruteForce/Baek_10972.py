"""
    @ 10972. 다음 순열
    @ Prob. https://www.acmicpc.net/problem/10972
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 02. 23.
    @ End day: 20. 02. 23.
"""

from itertools import permutations

N = int(input())
arr = tuple(map(int, input().split()))
permutation_arr = list(permutations([(i+1) for i in range(N)], N))

#i = 0
#for a in permutation_arr:
#    print(i, a)
#    i += 1

location = permutation_arr.index(arr)
if location >= len(permutation_arr)-1:
    print(-1)
else:
    print(*permutation_arr[location+1])

"""
4
1 2 3 4
>
1 2 4 3

4
1 4 2 3
>
1 2 4 3

4
1 3 4 2

5
5 4 3 2 1
>
-1
"""