class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.last = None
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self):
        self.next = next

    def getNext(self):
        return next

    def setLast(self, last):
        self.last = last

    def getLast(self):
        return self.last

    def __str__(self):
        return self.getData()

class Queue(object):

    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.curr = None
        self.size = 0

    def enQueue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
            self.size += 1

    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.rear.getData()

    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty")
            raise IndexError
        return self.front.getData()

    def deQueue(self):
        if self.rear is None:
            print("Sorry, the queue is empty")
            raise IndexError
        result = self.rear.getData()
        self.rear = self.rear.last
        self.size -= 1
        return result

    def size(self):
        return self.size

    def PrintWholeQueue(self):
        result = ""
        if self.front is None:
            print("Queue is empty")
            return
        self.curr = self.front.getNext()
        print("Here" + self.curr.getData())

        return
'''
        result += self.front.getData()
        self.curr = self.front.getNext()
        while self.curr is not None:
            print(self.curr.getData())
            self.curr.setNext(self.curr.getNext())

        print(result)
'''


q = Queue()
q.enQueue("first")
print("Front: " + q.queueFront())
print("Rear: " + q.queueRear())
q.enQueue("second")
print("Front: " + q.queueFront())
print("Rear: " + q.queueRear())
q.enQueue("third")
print("Front: " + q.queueFront())
print("Rear: " + q.queueRear())
