# 📖 Database Essential Concept Part1
- 주제: 
- ⏳ 최초 생성: 19. 09. 21
- ⌛ 마지막 작업: 19. 09. 21

## 📋 Introduce of Database Concept.
- 관계형 데이터 모델을 기반으로 데이터베이스를 다룹니다. 관계형 데이터 모델이 무엇이며 키에 대해서 살펴볼 것입니다.
- SQL 쿼리문을 사용해서 관계형 데이터 모델을 조작해볼 것입니다. 
- 데이터베이스의 장애가 일어날 수 있음을 이해하고 이를 회복하는 방법에 대해서 볼 것입니다.
- 마지막으로 관계형 데이터 모델을 설계해보고 정규식의 필요성에 대해서 살펴볼 것입니다. 

## 📋 관계형 데이터 모델의 개념
#### 용어정리

+ **속성(Attribute):** 릴레이션의 열. 
+ **튜플(Tuple):** 릴레이션의 행.
+ **도메인(Domain):** 속성 하나가 가질 수 있는 모든 값의 집합. 더는 분해할 수 없는 원자 값만 사용. 
+ **널 값(Null Value):** 특정 튜플의 속성 값을 모르거나, 적합한 값이 없는 경우 널(null)이라는 특별한 값 사용.
+ **차수(degree)**: 하나의 릴레이션에서 속성 전체 개수.
+ **카디널리티(Cardinality)**: 하나의 릴레이션에서 튜플 전체 개수.
+ **릴레이션 스키마(Relation Schema)**: 릴레이션의 이름과 릴레이션에 포함된 모든 속성의 이름으로 정의하는 릴레이션의 논리적 구조. 
+ **릴레이션 인스턴스(Relation Instance)**: 어느 한 시점에 릴레이션에 존재하는 튜플들의 집합. 

#### 릴레이션의 특성
+ **(1)튜플의 유일성**
    - 하나의 릴레이션에는 동일한 튜플이 존재할 수 없습니다. 릴레이션에서 하나의 튜플을 특정하기 위해서 키(Key) 개념을 알아야 합니다. 
+ **(2)튜플의 무순서**
    - 튜플의 순서가 바뀐다고 해서 다른 릴레이션이 아닙니다. 
+ **(3)속성의 무순서**
    - 하나의 릴레이션에서 속성 사이의 순서는 의미가 없습니다.
+ **(4)속성의 원자성**
    - 속성 값으로 원자 값만 사용할 수 있습니다. 즉 하나의 속성은 여러 값을 갖을 수 없습니다. 예를 들어 (학생, 교수)와 같이 직위 속성에 두 개의 값을 갖을 수 없습니다. 

## 📋 키
#### 키란?
+ 릴레이션에 포함된 튜플을 유일하게 구분해주는 역할을 키가 합니다. 키의 종류로는 (1)슈퍼키 (2)후보키 (3)기본키 (4)대체키 (5)외래키가 있습니다.
 
#### 키의 종류
| 고객 아이디 | 고객명 | 나이 | 직업 | 전화번호 | 
| :----------: | :---------: | :----------: | :----------: | :----------: |
|  apple  |  김민준     |   22    |   직장인     | 010-2222-1111   |
|  orange   |  한서연     |   27    |  대학원생      |  010-2222-3333  |
|  here   |  임다은     |   15    |   학생     |  010-3333-44444  |
|  loveme   |  박우진    |   18    |    학생    | 010-5555-66666   |

+ **수퍼키(Super Key)**
    - 유일성의 특성을 만족하는 속성 또는 속성들의 집합입니다.  
    - `직업`은 값이 같은 고객이 존재할 수 있으므로 수퍼키가 될 수 없습니다. `고객명` 또한 동명이인이 존재할 수 있으므로 슈퍼키가 될 수 없습니다. 
    - 중복 아이디 생성을 허용하지 않는 홈페이지라면 `고객 아이디` 속성은 수퍼키가 될 수 있습니다.
    - `(고객 아이디, 고객명)` 속성 집합은 수퍼키가 될 수 있습니다.
    - `(고객 아이디, 고객명)`과 같이 하나의 튜플을 구별하기 위해서 불필요한 속성의 값까지 확인할 수 있습니다. 이는 비효율적인 작업이므로 꼭 필요한 속성의 집합만을 유일하게 구분할 수 있도록 **후보키** 개념이 필요합니다.
    
+ **후보키(Candidate Key)**
    - 유일성과 최소성을 만족하는 속성 또는 속성들의 집합입니다. 최소성은 키를 구성하는 여러 속성 중에 하나라도 없으면 튜플을 유일하게 구별할 수 없는 꼭 필요한 최소한의 속성들로만 키를 구성하는 특성입니다. 
    - `고객 아이디`는 후보키가 될 수 있습니다. 
    - `(고객 아이디, 고객이름)`은 후보키가 될 수 없습니다. 왜냐하면 `고객 아이디`만으로 튜플을 유일하게 구분할 수 있기 때문입니다.
    
+ **기본키(Primary Key)**
    - 릴레이션에서 튜플을 구별하기 위해 여러 개의 후보키를 사용할 필요는 없습니다. 데이터베이스 설계자는 여러 후보키 중에서 기본적으로 사용할 키를 선택하는데 이것이 **기본키**입니다.
    - **후보키**가 여러개라면 데이터베이스 사용 환경을 고려해서 적합한 것을 후보키로 사용합니다. 
    - 기본키를 정할 때 다음 두 가지를 고려해야합니다.
        + 기본키가 널 값인 튜플은 다른 튜플과 구별하여 접근하기 어려우므로 **널 값을 가질 수 있는 속성은 기본키로 부적절합니다.**  
        + 값이 자주 변경되는 속성으로 구성된 후보키를 기본키로 선택하면 값이 변경될 때마다 기본키로 적합한지 검사해야하므로 **값이 자주 변경될 수 있는 속성이 포함된 후보키는 기본키로 부적절합니다.**
        + **단순한 후보키를 기본키로 선택하세요**
          
+ **대체키(Alternative Key)**
    - 기본키로 선택되지 못한 후보키들입니다. 
    - 대체키는 기본키를 대체할 수 있지만 기본키가 되지 못하고 탈락하였습니다.
    

+ **외래키(Foreign Key)**
    - 어떤 릴레이션에 소속된 속성 또는 속성 집합이 다른 릴레이션의 기본키가 되는 키입니다. 
    - 다른 릴레이션이 기본키를 그대로 참조하는 속성의 집합이 외래키입니다.  

![key.jpg](https://github.com/KoEonYack/LevelUp-Algorithm/blob/master/InterviewQuestion/Database/img/key.jpg?raw=true)

### Reference
+ [데이터베이스 개론 : 기초 개념부터 빅 데이터까지 큰 흐름이 보이는 데이터베이스 교과서 (한빛출판사, 김연희 저)](https://terms.naver.com/list.nhn?cid=58430&categoryId=58430)
+ [Github ChangYeop-Yang/Study-DataBase](https://github.com/ChangYeop-Yang/Study-DataBase)