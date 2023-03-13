#Stack implementation using OOP

class Stack:
    
    def __init__(self):
        #constructor function
        self.stack = []
    def push(self,data):
        #adds element on to the stack
        self.stack.append(data)
    
