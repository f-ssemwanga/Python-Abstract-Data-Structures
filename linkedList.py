class Node():
    #This will be a subclass of the linked list
    
    def __init__(self, data=None):
        #node constructor
        #data is the data point to be stored in the node
        self.data  = data
        self.next = None # pointer to the next node - last node's next pointer is None by default