'''
    @ 42. 이분검색
    @ Idea. 이분검색
    @ TestCase:
        input:  8 32
                23 87 65 12 57 32 99 81
        output: 3
    @ Start day: 19. 10. 10
    @ End day: 19. 10. 10
'''

N, key = 8, 32
a = [23, 87, 65, 12, 57, 32, 99, 81]
a.sort()
rt = len(a) - 1
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

