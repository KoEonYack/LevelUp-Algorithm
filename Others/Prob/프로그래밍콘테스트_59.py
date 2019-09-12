'''
    @ 프로그래밍 콘테스트 - 구간 스케줄링 문제
    @ Prob. 59p
    @ Algo:
    @ Start day: 19. 09. 12
    @ End day: 19. 09.
'''

# input 5 (강의 갯수)
# s = "1 2 4 6 8"
# t = "3 5 7 9 10"
# output = 3

import operator

NunOfLec = int(input("Input num of lecture>"))

startTimeStr = input("Input start time>")
startTime = list(map(int, startTimeStr.split()))

endTimeStr = input("Input end time>")
endTime = list(map(int, endTimeStr.split()))

dic = {}

for i in range(NunOfLec):
    dic[startTime[i]] = endTime[i]

sorted_endTimeListTuple = sorted(dic.items(), key=operator.itemgetter(0))
print(sorted_endTimeListTuple)
t = 0
ans = 0
for key, value in sorted_endTimeListTuple:
    if t < key:
        ans += 1
        t = value
        print("Lecture time: "  + str(key) + ":" + str(value))

print(ans)