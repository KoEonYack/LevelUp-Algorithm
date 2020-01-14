"""
    @ Baek 10984
    @ Prob. https://www.acmicpc.net/problem/10984
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 14
    @ End day: 20. 01. 14
"""

T = int(input())
for i in range(T):
    subject_num = int(input())
    grade = 0
    score = 0
    for j in range(subject_num):
        input_grade, input_score = map(float, input().split())
        grade += input_grade
        score += input_score * input_grade
    print(int(grade), "%.1f" % (score/grade))


"""
2
4
3 4.3
2 2.0
4 0.0
2 4.0
3
4 0.0
4 0.0
3 0.0
>
11 2.3
11 0.0
"""