


def collision(speed, pos):
    ans = 0

    for i in range(len(speed)):
        speed[i] = speed[i] * 10000000

    for i in range(len(speed)):
        if i < pos and speed[pos]+pos <= speed[i]+i:
            ans += 1
        elif i > pos and speed[pos]+pos >= speed[i]+i:
            ans += 1

    #for i in range(len(speed)):
    #    print("i", i, ":", speed[i] + i)

    return ans

#print(collision([6, 6, 1, 6, 3, 4, 6, 8], 2)) # 2
#print(collision([8, 3, 6, 3, 2, 2, 4, 8, 1, 6], 7)) #2
#print(collision([1, 3, 7, 4, 6, 4], 3)) #1
#print(collision([3, 2, 1], 2)) #1
print(collision([1, 3, 7, 4, 6, 4], 3)) #1


# 충돌
# 이전에 출발한 것보다 값이 작은 경우
# 이후에 출발한 것보다 값이 큰 경우