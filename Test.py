


from queue import PriorityQueue
que = PriorityQueue()
que.put((-1, 1))
que.put((-2, 2))

for i in range(len(que.queue)):
    print (que.queue[i][-1])