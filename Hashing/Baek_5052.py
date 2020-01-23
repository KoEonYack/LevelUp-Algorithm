"""
    @ 5052 전화번호 목록
    @ Prob. https://www.acmicpc.net/problem/5052
     Ref.
    @ Algo: Hashing
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

import sys
input = sys.stdin.readline

def solve(contacts):
    print(contacts)
    contacts.sort()

    st = contacts[0]

    for contact in contacts[1:]:
        print(st, contact)
        if st in contact:
            return "NO"
        else:
            st = contact

    return "YES"


for i in range(int(input())):
    n = int(input())
    contacts = []

    for j in range(n):
        contacts.append(input().rstrip())

    print(solve(contacts))

"""
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
>
NO
YES
"""