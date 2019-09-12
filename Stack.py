class Stack(object):
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) > self.limit:
            print("Stack Overflow!")
        else:
            self.stk.append(item)
        # PRINT

    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
        else:
            self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
        else:
            print(self.stk[-1])

    def size(self):
        if len(self.stk) == 0:
            print("Stack is empty")
        else:
            print("Size of Stack: " + len(self.stk))

    def RemoveStack(self):
        pass

    def PrintStack(self):
        for i in range(len(self.stk)):
            print("[" + str(self.stk[i]) + "]->")
        print("[HEAD]")



def MENU():
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("9. Show Stack")
    print("0. Quit")
    select = int(input("Select Menu>"))
    return select

if __name__ == "__main__":
    stack = Stack()
    while True:
        select = MENU()
        if select == 1: # Push
            number = int(input("Which number you want to input stack>"))
            stack.push(number)
            stack.PrintStack()

        elif select == 2: # Pop
            stack.pop()

        elif select == 3: # Peek
            stack.peek()

        elif select == 9: # Show stack
            stack.PrintStack()

        elif select == 0:
            print("End of Program")
            exit(0)

        else:
            print("Wrong Input")
