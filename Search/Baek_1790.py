"""
    @ Baek 1790 수 이어 쓰기 2
    @ Prob. https://www.acmicpc.net/problem/1790
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 02. 12.
    @ End day: 20. 02. 12.
"""

def digitNum(num):
    ans = 0
    i = 1
    max_digit = 9

    while True:
        if (max_digit + 1) > num:
            ans += ((N - pow(10, i-1) + 1) * i)
            break
        else:
            #print(max_digit, pow(10, i-1), i)
            ans += (max_digit - pow(10, i-1) + 1) * i
        i += 1
        max_digit = max_digit * 10 + 9

    return ans

def binary_search(N, target):
    start = 0
    end = N

    while start <= end:
        mid = (start + end) // 2
        cal_num = digitNum(mid)
        #print(mid, cal_num, target)
        if cal_num == target:
            return mid
        elif cal_num < target:
            start = mid + 1
        else:
            end = mid - 1


N, K = map(int, input().split())
print(binary_search(N, K))
#print(digitNum(N))


"""
20 23
> 
6
"""