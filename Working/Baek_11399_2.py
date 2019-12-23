'''
    @ Baek 11399
    @ Prob. https://www.acmicpc.net/problem/11399
      Ref. http://blog.naver.com/PostView.nhn?blogId=occidere&logNo=220790825104&parentCategoryNo=&categoryNo=14&viewDate=&isShowPopularPosts=false&from=postView
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 23.
    @ End day: 19. 12. 23.
'''


def solution():
    answer = 0

    for i in range(N):
        for j in range(0, i+1):
            answer += arr[j]

    return answer


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(solution())

'''
5
3 1 4 3 2
[ 3 1 4 3 2 ]
3
3 + 3
2 + 3 + 4 
'''