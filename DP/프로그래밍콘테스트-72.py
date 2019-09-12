'''
    @ 프로그래밍 콘테스트 - 배낭문제
    @ Prob. 71p
    @ Algo: Dynamic Programming
    @ Start day: 19. 09. 12
    @ End day: 19. 09. 12
'''

# 입력 n = 4
# (w, v) = {(2, 3), (1, 2), (3, 4), (2, 2)}
# W = 5
# 출력 7 (0, 1, 3)

# param: i 탐색 갯수, j 가방의 가치

def rec(i, j):
    result = 0

    if i >= N:                                  # 더 이상 넣을 물건이 없다.
        print("더 이상 넣을 물건이 없습니다.(물건에 대한 탐색을 마쳤습니다.)")
    elif j < W[i]:                              # 이 물건은 들어가지 않는다.
        result = rec(i+1, j)
    else:                                       # 물건을 넣는 경우와 넣지 않는 경우에 대해서 조사
        result = max(rec(i+1, j), rec(i+1, j-W[i])+V[i])

    return result


N = int(input("넣을 수 있는 물건의 갯수를 입력해주세요"))
BagW = int(input("가방에 넣을 수 있는 물건의 무게를 입력해주세요"))

W_Str = input("Input Weight>")
W = list(map(int, W_Str.split()))

V_Str = input("Input Value>")
V = list(map(int, V_Str.split()))
print(rec(0, W))