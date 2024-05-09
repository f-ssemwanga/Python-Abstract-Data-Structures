# oop Queue Implementation


class Queue:
    """simulation of a queue ADT"""

    def __init__(self):
        """queue constructor"""
        self.max = 5  # length of queue
        self.front = self.rear = -1  # pointers
        self.items = []
        self.removedItem = 0
