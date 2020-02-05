"""
    @ 1744. 수 묶기 [실패]
    @ Prob. https://www.acmicpc.net/problem/1744
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

# 음수는 가작 작은 수 끼리
#   -> 음수 중에서 가장 작은 수끼리 묶는다.
#   -> 외토리 음수는 0을 곱한다.
# 양수는 가장 큰 수 끼리
#   -> 1은 안묶는다.

arr = []
N = int(input())
for i in range(N):
    arr.append(int(input()))

pos_arr = []
neg_arr = []

zero_flag = False
one_flag = False
for i in range(N):
    if arr[i] >= 0:
        if arr[i] == 0:
            zero_flag = True
        elif arr[i] == 1:
            one_flag = True
        pos_arr.append(arr[i])
    else:
        neg_arr.append(arr[i])

pos_arr.sort(reverse=True)
neg_arr.sort()
result = 0

for i in range(0, len(neg_arr)-1, 2):
    result += neg_arr[i] * neg_arr[i+1]
    #print("test", result, neg_arr[i], neg_arr[i+1])

#print("here ", result)

for i in range(0, len(pos_arr)-1, 2):
    #print(pos_arr[i])
    if pos_arr[i] == 0:
        continue
    if pos_arr[i] == 1:
        result += 1
        continue
    if pos_arr[i+1] == 0:
        result += pos_arr[i]
    else:
        result += pos_arr[i] * pos_arr[i+1]

    print("DEBUG:", result, pos_arr[i], pos_arr[i+1])

print("--------")
print(result)


if zero_flag is False and one_flag is True:
    result += 1
if len(pos_arr) % 2 == 1:
    if pos_arr[-1] != 1:
        result += pos_arr[-1]
if len(neg_arr) % 2 == 1:
    #print("zere_flag", zero_flag, result)
    if zero_flag is not True: # 0이면 상쇄되니깐 고민할 필요가 없다.
        #print("here", result)
        result += neg_arr[-1]
print(result)

"""
5
1
2
3
4
5




7
-6
-2
-3
0
2
3
4
-------------------




4
-1
2
1
3

>
6
"""




