N, M = map(int, input().split())

if N < M:
    print("<")
elif N > M:
    print(">")
else:
    print("==")