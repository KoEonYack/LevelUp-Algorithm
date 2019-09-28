def solution(bishops):
    answer = 0
    pos = []
    ArrMap = [[0] * 9 for _ in range(9)]
    PosArr = []

    # 비숍 배열 입력 처리
    for bishop in bishops:
        #print(bishop)
        if bishop[0] is 'A':
            pos.append([1, int(bishop[1])])
        if bishop[0] is 'B':
            pos.append([2, int(bishop[1])])
        if bishop[0] is 'C':
            pos.append([3, int(bishop[1])])
        if bishop[0] is 'D':
            pos.append([4, int(bishop[1])])
        if bishop[0] is 'E':
            pos.append([5, int(bishop[1])])
        if bishop[0] is 'F':
            pos.append([6, int(bishop[1])])
        if bishop[0] is 'G':
            pos.append([7, int(bishop[1])])
        if bishop[0] is 'H':
            pos.append([8, int(bishop[1])])

    # 비숍 이동 좌표 처리
    for a_pos in pos:

        curr_bi_x, curr_bi_y = a_pos[0], a_pos[1]
        PosArr.append([curr_bi_x, curr_bi_y])
        xx, yy = curr_bi_x, curr_bi_y
        while xx <= 8 and xx >= 1 and yy <= 8 and yy >= 1: # 1사분면
            if xx+1 <= 8 and xx+1 >= 1 and yy+1 <= 8 and yy+1 >= 1 :
                PosArr.append([xx+1, yy+1])
            xx, yy = xx+1, yy+1
        xx, yy = curr_bi_x, curr_bi_y

        while xx <= 8 and xx >= 1 and yy <= 8 and yy >= 1 : # 2사분면
            if xx - 1 <= 8 and xx - 1 >= 1 and yy + 1 <= 8 and yy + 1 >= 1:
                PosArr.append([xx-1, yy+1])
            xx, yy = xx - 1, yy + 1
        xx, yy = curr_bi_x, curr_bi_y

        while xx <= 8 and xx >= 1 and yy <= 8 and yy >= 1: # 3사분면
            if xx - 1 <= 8 and xx - 1 >= 1 and yy - 1 <= 8 and yy - 1 >= 1 :
                PosArr.append([xx-1, yy-1])
            xx, yy = xx - 1, yy - 1
        xx, yy = curr_bi_x, curr_bi_y

        while xx <= 8 and xx >= 1 and yy <= 8 and yy >= 1: # 4사분면
            if xx + 1 <= 8 and xx + 1 >= 1 and yy - 1 <= 8 and yy - 1 >= 1 :
                PosArr.append([xx+1, yy-1])
            xx, yy = xx + 1, yy - 1

    #  and ([xx, yy] not in pos) and ([xx, yy] not in PosArr)

    remove_dup = list(set(map(tuple, PosArr)))
    for a in pos:
        if a in remove_dup:
            remove_dup.remove(a)

    for b in pos:
        if b in remove_dup:
            remove_dup.remove(a)

    return 64 - (len(remove_dup))
    #return 64 - len(PosArr)

print(solution(["D5", "E8", "G2"]))

'''
a = [[4, 5]]
print(a[0][1])
'''

