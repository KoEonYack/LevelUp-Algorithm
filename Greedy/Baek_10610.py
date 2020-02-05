


arr = [int(i) for i in input()]
arr.sort(reverse=True)

if arr[-1] == 0 and sum(arr) % 3 == 0:
    print("".join(map(str, arr)))
else:
    print(-1)
