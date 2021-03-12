

# K, N = map(int, input().split())
K, N = 1, 3
STEP_1 = ["R", "D", "L", "U"] 
STEP = []
MAP = [[""] * N for _ in range(N)]
x, y = 0, 0
if K == 1:
    STEP = STEP_1
    x, y = 0, 0

step_idx = 0
dirs = STEP[step_idx]
rep = 1
while rep != N*N:
    if dirs == "R":
        if 0 <= x < N-1:
            if MAP[y][x] == "":
                x += 1
                MAP[y][x] = str(rep)
                rep += 1
            else:
                x += 1
        elif x == N-1:
            step_idx = (step_idx+1) % 4
            dirs = STEP[step_idx]
    elif dirs == "D":
        if 0 <= y < N-1:
            if MAP[y][x] == "":
                y += 1
                MAP[y][x] = str(rep)
                rep += 1
            else:
                x += 1
        elif y == N-1:
            step_idx = (step_idx+1) % 4
    
    print("===========")
    print(dirs)
    for a in MAP:
        print(a)
    

