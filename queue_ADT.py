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
