'''
    Queue - Fixed Size
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
            print("Queue Overflow!")
        else:
            self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1
        print("Add ", item)

    def deQueue(self):
        if self.size <= 0:
            print("Queue Underflow")
            return 0
        else:
            popVal = self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print("Pop Value: " + str(popVal))

    def queueRear(self):
        if self.rear is None:
            print("Stack is Empty")
            raise IndexError
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.que[self.front]

    def size(self):
        return self.size

    def PrintWholeQueue(self):
        result = ""
        for i in range(len(self.que)):
            result += "[" + str(self.que[i]) + "] -> "
        result += "HEAD"
        print(result)

def MENU():
    print("1. Enqueue.")
    print("2. Dequeue.")
    print("3. Is empty?")
    print("9. Show Whole Stack.")
    print("0. Quit.")
    select = int(input("Select Menu>"))
    return select

if __name__ == "__main__":
    q = Queue()
    q.enQueue(3)
    q.enQueue(4)
    q.deQueue()