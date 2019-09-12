'''
    Queue - Dynamic

'''

class Queue(object):
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("Enqueue: " + item)

    def deQueue(self):
        if self.size <= 0:
            print("Queue Underflow")
            return 0
        else:
            popValue = self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size -1
            print("Pop: " + popValue)

    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty")
            raise IndexError
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.que[self.front]

    def size(self):
        return self.size()

    def resize(self):
        newQue = list(self.que)
        self.limit = 2 * self.limit
        self.que = newQue