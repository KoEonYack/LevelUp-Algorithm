import copy
def travel(answer_set,answer,start,K,count):
    answer.append(start)
    if count==K:
        return True
    try:
        answer_set[start]
    except:
        answer.pop()
        return False
    for i in range(len(answer_set[start])):
        end=answer_set[start][i]
        count+=1
        temp_set=copy.deepcopy(answer_set)
        temp_set[start]=temp_set[start][:i]+temp_set[start][i+1:]
        boolean=travel(temp_set,answer,end,K,count)
        if boolean:
            return True
        else:
            count-=1
    answer.pop()
    return False
def solution(tickets):
    answer_set={}
    for ticket in tickets:
        if ticket[0] in answer_set:
            answer_set[ticket[0]].append(ticket[1])
            answer_set[ticket[0]].sort()
        else:
            answer_set[ticket[0]]=[ticket[1]]
    answer=[]
    count=0
    start="ICN"
    travel(answer_set,answer,start,len(tickets),count)
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

