"""
    @ 18 kako blind: 셔틀버스
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/17678
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def time_to_int(t): 
    h, m = [int(x) for x in t.split(':')]
    return h * 60 + m

def int_to_time(i):
    h, m = divmod(i, 60)
    return f'{h:02d}:{m:02d}'
    
# n회, t분 간격, m명 탑승 가능
def solution(n, t, m, timetable):
    line_up = sorted([time_to_int(t) for t in timetable])
    last_bus = 60 * 9 + (n - 1) * t
    
    # n 번의 버스가 옴 
    # m 명 탑승 가능 
    for i in range(n):
        if len(line_up) < m: return int_to_time(last_bus) 
        
        if i == n - 1:
            if line_up[0] <= last_time:
                last_time = line_up[m-1] - 1
            return int_to_time(last_time)
        
        bus_arrive_time = (60 * 9) + i * t 
        for j in range(m-1, -1, -1): # m명의 사람들 
            if timetable[j] <= bus_arrive_time:
                print(bus_arrive_time)
                del line_up[j]
        
    return 

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable)) # 09:00

