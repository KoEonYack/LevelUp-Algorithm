"""
    @ 42840. 모의고사
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42840
     Ref.   https://programmers.co.kr/learn/courses/30/lessons/42840/solution_groups?language=python3
    @ Algo: Brute force
    @ Start day: 20. 03. 02.
    @ End day: 20. 03. 02
"""

def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    f_ans = 0
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    s_ans = 0
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    t_ans = 0

    i = 0
    for num in answers:
        if first[i % len(first)] == num:
            f_ans += 1
        if second[i % len(second)] == num:
            s_ans += 1
        if third[i % len(third)] == num:
            print("DE", third[i % len(third)])
            t_ans += 1
        i += 1

    tmp = []
    tmp.append(f_ans)
    tmp.append(s_ans)
    tmp.append(t_ans)

    maxV = max(tmp)
    if maxV == f_ans:
        answer.append(1)
    if maxV == s_ans:
        answer.append(2)
    if maxV == t_ans:
        answer.append(3)

    #print(f_ans, s_ans, t_ans)
    return answer


print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]


"""
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
                       [1, 2, 3, 4, 5]
2번 수포자가 찍는 방식:   2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
                       [2, 1, 2, 3, 2, 4, 2, 5] 
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
                       [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
"""