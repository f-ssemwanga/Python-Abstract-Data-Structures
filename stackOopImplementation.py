#Stack implementation using OOP

class Stack:
    
    def __init__(self):
        #constructor function
        self.stack = []
    def push(self,data):
        #adds element on to the stack
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def peek(self):
        #returns the element on top of the stack
        return self.stack[-1]
    def dequeue(self):
        #removes peek element
        #check if the stack is not emipty
        if len(self.stack) <= 0:
            return "Stack is empty"
        else:
            removedElement = self.stack.pop()
            return f'removed: {removedElement}'
    def getStackSize(self):
        #returns the size of the stack
        return len(self.stack)
    def displayStack(self):
        #displays contents of the stack
        print(self.stack)
    
#Testing 
myStack = Stack()
for element in [5,6,9,6,7,12]:
    myStack.push(element)
print(f'There are {myStack.getStackSize()} elements in the stack')
myStack.displayStack()
print(f'The peek element in the stack is: {myStack.peek()}')
for i in range(3):
    myStack.dequeue()

print(f'The peek element in the stack is: {myStack.peek()}')
myStack.displayStack()

