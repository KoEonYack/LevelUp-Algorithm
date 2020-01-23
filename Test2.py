from queue import PriorityQueue
numbers, Q = [9, 1, 4, 5], PriorityQueue()
for number in numbers:
    Q.put((-number, number))

while not Q.empty():
    print (Q.get())