# Tree
---------------

## 용어 정리
- 트리에서의 위치 
    * **루트 노드**: 트리의 첫 번쨰 노드
    * **단말 노드**: 자식 노드가 없는 노드
    * **내부 노드**: 자식 노드가 있는 노드 

- 노드 사이의 관계
    * **부모 노드**: 부모와 자식 노드는 간선으로 연결되어 있음
    * **자식 노드**: 부모와 자식 노드는 간선으로 연결되어 있음
    * **선조 노드**: 루트 노드로부터 부모 노드까지의 경로 상에 있는 노드
    * **후손 노드**: 특정 노드의 아래에 있는 노드
    * **형제 노드**: 같은 부모의 자식 노드

- 노드 속성
    * **레벨**: 루트 노드로부터의 거리
    * **높이**: 루트 노드로부터 가장 먼 거리에 있는 자식 노드의 높이에 1을 더한 값
    * **차수**: 한 노드가 가지는 자식 노드의 개수

- 
    * **포리스트**: 트리의 집합, 여러개의 트리를 모아 놓은 것.
    * **이진 트리**: 모든 트리 노드의 차수가 2 이하인 트리.
    * **포화 이진 트리**: 모든 레벨의 노드가 꽉 차 있는 이진 트리.
        * ``` n =  2^h - 1 (n: 높이 h인 이진 포화 트리의 노드 갯수)  ```
    * **완전 이진 트리**: 높이가 h고 노드 개수가 n개라고 하였을 때 레벨 1부터 h-1까지는 포화 이진 트리와 마찬가지로 꽉 채워져 있다가 마지막 레벨 h에서는 왼쪽에서 오른쪽으로 노드가 채워져 있는 이진 트리를 말한다. 즉, 마지막 레벨 h에서는 노드가 왼쪽부터 차례로 채워져 있어야 하며 중간에 빈 노드가 있어서는 안된다. 
        * ``` n <  2^h - 1 (n: 높으 h인 이진 포화 트리의 노드 갯수. 단, 노드 번호(n+1)번 부터 2^h - 1까지는 공백)  ```
    * **편향 이진 트리**: 같은 높이의 이진 트리 중에서 최소 개수의 노드 개수를 가지면서 왼쪽 혹은 오른쪽으로만 편향되게 서브트리를 가지는 이진트리를 말함.
    * **이진 연결 트리**: 포인터로 구현한 이진 트리.

- 트리 속성
    * ``` 트리에서 노드 갯수가 1개일 때 간선의 개수는 n - 1이다. ```
        * 루트 노드를 제외한 나머지 노드는 간선이 1개씩 존재하기 때문.
        
- 우선순위 큐(Priority queue)
    - 다음과 같은 조작을 할 수 있는 데이터 구조를 우선순위 큐라고 한다.
        - [1] 수를 추가한다.
        - [2] 최소 수치를 뽑아 낸다.(값을 취득하고, 삭제한다.)
    - 우선순위 큐는 이진트리를 이용해서 구현할 수 있고 이를 **힙**이라고 한다. 
    - 힙에는 여러 종류가 있는데 주로 이진 힙이라는 데이터구조를 볼 것이다. 