"""
    @ 2020 카카오 인턴. 키패드 누르기
    @ Prob. 
      Ref. https://github.com/coco-in-bluemoon/programmers-challenges/blob/master/2020%20%EC%B9%B4%EC%B9%B4%EC%98%A4%20%EC%9D%B8%ED%84%B4%EC%8B%AD/%ED%82%A4%ED%8C%A8%EB%93%9C%20%EB%88%84%EB%A5%B4%EA%B8%B0.py
    @ Algo: 시뮬레이션
    @ Start day: 20. 10. 22.
    @ End day:   20. 10. 22.
"""




def solution(numbers, hand):
    numbers = [str(number) for number in numbers]

    cur_left = '*'
    cur_right = '#'

    left_numbers_set = '147*'
    right_numbers_set = '369#'

    ans = ''
    for number in numbers:
        if number in left_numbers_set:
            cur_left = number
            ans += 'L'
        elif number in right_numbers_set:
            cur_right = number
            ans += 'R'
        else:
            