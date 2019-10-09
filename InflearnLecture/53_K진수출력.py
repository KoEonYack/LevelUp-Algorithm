'''
    @ 53. K진수 출력
    @ Idea. 스택
    @ TestCase:
        input: 11 2
        output: 1011

        input: 31 16
        output: 1F
    @ Start day: 19. 10. 09
    @ End day: 19. 10. 09
'''


N, K = map(int, input().split())
result = []
data = "0123456789ABCDEF"

while N > 0.001:
    tmp = int(N % K)
    result.append(data[tmp])
    N = int(N) / K
    #print(N)

print("".join(result[:-1]))