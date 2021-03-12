"""
    @ Baek 1700. 멀티탭 스케줄링
    @ Prob. https://www.acmicpc.net/problem/1700
     Ref.   https://alpyrithm.tistory.com/71
    @ Algo: BFS
    @ Start day: 20. 09. 24.
    @ End day: 20. 09. 24. 
"""




"""
우선 멀티탭이 비어있는지, 혹은 꽂으려고 하는 플러그가 있는지 확인을 한다.
  -> 둘중 하나가 True라면 해당 플러그를 꽂고 continue해준다.

아니라면 플러그 하나를 뽑아야 한다.
  -> 다시 사용되지 않는 플러그를 우선적으로 뽑아주고
  -> 꽂혀있는 플러그중에서 가장 나중에 사용되는 플러그를 뽑아준다.
"""



"""
2 7
2 3 2 3 1 2 7
>
2

"""