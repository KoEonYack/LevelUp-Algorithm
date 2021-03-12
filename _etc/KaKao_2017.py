'''
    @ 카카오 2017: 자연수의 합
    @ Prob. https://m.blog.naver.com/bsos1202/221090473029
    @ Start Day: 2019. 09. 20.
    @ End Day: 2019. 09. 20.
'''

def solution(v):
    answer = [0, 0]
    answer[0] = v[0][0] ^ v[1][0] ^ v[2][0]
    answer[1] = v[0][1] ^ v[1][1] ^ v[2][1]

    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))