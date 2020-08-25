if __name__ == "__main__":

    enable = {str(i) for i in range(10)}  # 0, 1, 2 ... 9 (가능한 수)

    # input
    N = int(input())  # 이동하려고 하는 채널
    M = int(input())  # 고장난 버튼의 개수
    if M != 0:
        enable -= set(map(str, input().split()))  # 고장난 버튼 리스트 제거

    # case1 (100번에서 +, - 로만 움직이는 경우)
    min_cnt = abs(100 - N)

    # case2 (1,000,000 채널까지 브루트 포스 진행)
    # 500,000 채널까지 존재하기 때문에 500,000 보다 크면서 모든 숫자의 경우를 거치는 1,000,000까지를 범위로 잡음
    for num in range(1000001):
        num = str(num)
        for j in range(len(num)):
            if num[j] not in enable:
                break
            elif j == len(num) - 1:
                min_cnt = min(min_cnt, abs(N - int(num)) + len(str(num)))
    print(min_cnt)
