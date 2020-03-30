from queue import PriorityQueue

que = PriorityQueue()

que.put(4)
que.put(10)
que.put(2)

for i in range(len(que.queue)):
    print(que.queue[i], end=" ")


print(que.get())
print(que.get())


## 작은 것 부터 나온다.