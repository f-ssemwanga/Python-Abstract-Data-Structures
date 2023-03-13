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