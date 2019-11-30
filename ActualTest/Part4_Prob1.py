'''
    Part4 - Prob1. : BruteForce

    sol. Left는 하나씩 검색을 하는 것이다.
        Right은 최댓값을 구하는 것이다.

    Ref. https://incastle-study.tistory.com/2
'''

def trapping_rain(buildings):
    raindrop = 0
    for i in range(len(buildings)):
        # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이
        print("---------------------------------------")
        max_left = max(buildings[:i+1])
        print("left: ", buildings[:i+1])

        # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이
        max_right = max(buildings[i:])
        print("right: ", buildings[i:])

        # 둘중에 최솟값
        which_low = min(max_left, max_right)

        # 절대값 주의
        raindrop = raindrop + abs(buildings[i] - which_low)
        print(buildings[i], which_low)
        #print(raindrop)
    return raindrop


print(trapping_rain([3, 1, 2, 3, 4, 1, 1, 2]))
#print(trapping_rain([6, 0, 0, 0, 0]))