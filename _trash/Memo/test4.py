

from itertools import product
import sys


target = input()
N = int(input())
arr = list(map(str, input().split()))
total = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
arr = total.difference(set(arr))
print("setOp", arr)
diff = sys.maxsize
remocon_num = 0

print("target/ ", len(target))
for i in product(arr, repeat=len(target)): # TODO: N개가 주어질 뿐이고 실제 만들어야하는 것은 target의 길이 
    i = int("".join(i))
    if diff > abs(int(target) - i):
        print("for / ", target, i)
        diff = abs(int(target) - i)
        remocon_num = i


print(remocon_num)
print(len(target) + abs(int(target) - remocon_num))


"""
5457
3
6 7 8
>
6

100
5
0 1 2 3 4
>
0
"""