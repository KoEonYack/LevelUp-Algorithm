"""
    @ Baek 1700 멀티탭 스케줄링
    @ Prob. https://www.acmicpc.net/problem/1700
      Ref.
      Ref Prob.
    @ Algo: Brute-force
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

# N: 콘센트 갯수
N, K = map(int, input().split())
arr = list(map(int, input().split()))
code = []
ans = 0
dis_max = 0
max_idx = 0
flag = False
for i in range(len(arr)):
    if arr[i] in code:                           # 이미 코드에 꼽혀있다.
        continue
    if N > len(code) and arr[i] not in code:     # 코드가 비어있다
        code.append(arr[i])
    else:                                        # 다 차고, 코드
        ans += 1
        for j in range(len(code)):
            dis = 0
            for k in range(i, N):
                dis += 1
                if code[j] == arr[k]:
                    flag = True
                    dis_max = dis
                    max_idx = k
                    break
            #print(code, arr[max_idx])
            if flag is True:
                code.remove(arr[max_idx])
                code.append(arr[i])
            elif flag is False:
                code.remove(code[-1])
                code.append(arr[i])

print(ans)

"""
2 7
2 3 2 3 1 2 7
>
2
------------------------------------
3 6
1 2 3 4 1 2
>
1
"""