"""
    T-Q1
    Start: 20. 08. 21.
    End:  20. 08. 21.
"""

import sys

a, b, c = map(int, input().split())
ans = -sys.maxsize

for n in range(a, b+1):
    res = [n]
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
            if n > b / 3 and c > 0:
                n += 10
                c -= 1
        res.append(n)
        if n == 1:
            ans = max(len(res), ans)
            break

print(ans)
            
"""

10 30 0
> 112

100 200 1
> 125
"""