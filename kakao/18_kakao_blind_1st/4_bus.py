"""
    @ 18 kako blind: 셔틀버스
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/17678
      Ref.
      
            https://github.com/jms7446/hackerrank/blob/d6c5d6d25dd6deb9de36415f4a8674f829a8a852/baekjoon/alg-study/w18/prog_17678.py
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 09. 08.
    @ End day: 20. 09. 08.
"""

def time_to_int(t): 
    h, m = [int(x) for x in t.split(':')]
    return h * 60 + m

def int_to_time(i):
    # return '%02d:%02d' % (last_time//60,last_time%60)
    return '%02d:%02d' % divmod(i, 60)
    # return f'{h:02d}:{m:02d}'
    
# n회, t분 간격, m명 탑승 가능
def solution(n, t, m, timetable):
    line_up = sorted([time_to_int(t) for t in timetable])
    num_of_crew = len(line_up)
    # line_up.append(time_to_int('23:59'))
    last_bus = 60 * 9 + (n - 1) * t
    
    # n 번의 버스가 옴 
    # m 명 탑승 가능
    idx_crew = 0
    for i in range(n):
        seat_left = m
        curr_bus_time = 60*9 + i*t 
        
        while seat_left > 0 and line_up[idx_crew] < curr_bus_time and idx_crew < num_of_crew:
            idx_crew += 1
            seat_left -= 1
            
            
    if seat_left > 0:
        return int_to_time(curr_bus_time)
    else:
        return int_to_time(line_up[idx_crew-1] - 1)
        

        
n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable)) # 09:00

