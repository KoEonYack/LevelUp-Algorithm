'''
    @ 43. 뮤직비디오 (이분검색 응용)
    @ Idea. 결정알고리즘
    @ TestCase:
        input:  9 3
                1 2 3 4 5 6 7 8 9
        output: 17
    @ Start day: 19. 10. 10
    @ End day: 19. 10. 10
'''


N, Part = 9, 3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 0

rt = sum(a) - 1
lt = 0

while rt >= lt:
    mid = int((rt + lt) / 2)
    if a[mid] == key:
        print(a[mid], mid)
        break
    elif a[mid] > key:
        rt = mid - 1
    elif a[mid] < key:
        lt = mid + 1

