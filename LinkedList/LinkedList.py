'''
    Linked List
    @ Ko-Eonyack
    @
'''

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.length = 0
        self.head = None

    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.Next != None

    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    '''
    Insert - 처음, 중간, 끝
    '''
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)

        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.selfNext(newNode)
        self.length += 1

    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count < pos-1:
                        count += 1
                        current = current.getNext()
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1

    '''
    Delete - 처음, 중간, 끝
    '''
    def deleteFromBeginning(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    def deleteLastNodeFromSinglyLinkedList(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.getNext() != None:
                previousnode = currentnode
                currentnode = currentnode.getNext()
            previousnode.setNext(None)
            self.length -= 1

    def deleteFromLinkedListWithNode(self, node):
        if self.length == 0:
            raise ValueError("List is empty")

        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                else:
                    previous = current
                    current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

    def deleteValue(self, value):
        currentnode = self.head
        previousnode = self.head
        while currentnode.next != None or currentnode.value != value:
            if currentnode.value == value:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode = currentnode
                currentnode = currentnode.next
        print("The value provided is not present")

    def deleteAtPosition(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head
        if pos > self.length or pos < 0:
            print("The position does not exist, Please enter valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def clear(self):
        self.head = None


    def printWholeNode(self):
        result = ""
        current = self.head
        if current is None:
            print("[노드에 저장된 값이 없습니다.]")

        while current != None:
            result += "[" + str(current.getData()) + "] -> "
            current = current.getNext()
        result += "Null"
        print(result)

if __name__ == "__main__":
    node = Node()
    while True:
        print("=========LinkedList=========")
        print("| [1] 노드의 맨 앞에 추가")
        print("| [2] 노드의 중간에 추가")
        print("| [3] 노드의 마지막에 추가")
        print("| [4] 노드 삭제")
        print("| [5] 전체 리스트 보기")
        print("| [6] Stress Test")
        print("| [7] Check Circular LinkedList")
        print("| [0] 프로그램 종료")
        print("============================")
        select = int(input("메뉴를 선택해 주세요>"))

        if select == 1:
            num = int(input("노드의 맨 앞에 저장할 값을 입력해 주세요>"))
            node.insertAtBeginning(num)
            node.printWholeNode()

        elif select == 2:
            num = int(input("노드에 저장할 값을 입력해 주세요>"))
            pose = int(input("값을 저장할 위치를 입력해 주세요>"))
            node.insertAtPos(pose, num)
            node.printWholeNode()

        elif select == 3:
            num = int(input("노드의 맨 앞에 저장할 값을 입력해 주세요>"))
            node.insertAtEnd(num)
            node.printWholeNode()

        elif select == 4:
            print("TODO")

        elif select == 5:
            node.printWholeNode()

        elif select == 6:
            print("TODO - stress test")

        elif select == 0:
            print("프로그램을 종료합니다.")
            exit(0)

        else:
            print("잘못 입력했습니다. 다시 입력해 주세요.")