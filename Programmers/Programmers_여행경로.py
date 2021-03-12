'''
    Programmers 여행경로
    Prob. https://programmers.co.kr/learn/courses/30/lessons/43164?language=java
    Ref. https://dailyheumsi.tistory.com/22
    Start Day: 2019. 09. 15
    End Day: 미완성 - 오름차순 경로 불가능
'''

def dfs(node, tickets, visit, temp, answer, cnt):
    answer.append(node)
    if cnt is len(tickets):
        return True

    for i in range(len(tickets)):
        if (tickets[i][0] is node) and (visit[i] is False):
            visit[i] = True
            success = dfs(tickets[i][1], tickets, visit, temp, answer, cnt+1)
            if success:
                return True
            visit[i] = False

    answer.pop()
    return False


def solution(tickets):
    temp = []
    answer = []
    visit = [False] * len(tickets)
    tickets = sorted(tickets, key=lambda x: x[0])
    dfs("ICN", tickets, visit, temp, answer, 0)
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

