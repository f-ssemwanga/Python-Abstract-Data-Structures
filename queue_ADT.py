# oop Queue Implementation


class Queue:
    """simulation of a queue ADT"""

    def __init__(self):
        """queue constructor"""
        self.max = 5  # length of queue
        self.front = self.rear = -1  # pointers
        self.items = []
        self.removedItem = 0

    def isEmpty(self):
        """Checks if the queue is empty"""
        if self.rear == -1 and self.front == -1:
            return True
        else:
            return False

    def isFull(self):
        """checks if the queue is full"""
        if self.rear == self.max - 1:
            return True
        else:
            return False

    def enqueue(self, item):
        """adds an item to the queue"""
        if self.isFull():
            return False
        elif self.isEmpty():
            self.rear = self.front = 0
            self.items.insert(self.rear, item)
        else:
            self.rear += 1
            self.items.insert(self.rear, item)

    def displayQueue(self):
        """displays the contents of the queue"""
        if self.isEmpty():
            print(f"Queue Items: {self.items}")
        else:
            print(f"Queue Front: {self.items [self.front]}")
            print(f"Queue Rear: {self.items[self.rear]}")
            print(f"Queue Items: {self.items}")
