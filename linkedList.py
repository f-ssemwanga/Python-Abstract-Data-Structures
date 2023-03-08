class Node():
    #This will be a subclass of the linked list
    
    def __init__(self, data=None):
        #node constructor
        #data is the data point to be stored in the node
        self.data  = data
        self.next = None # pointer to the next node - last node's next pointer is None by default
class LinkedList():
    #we will need a head node
    #the head node will contain no data
    def __init__(self):
        self.head = Node() # allows us to point to the first element in the list

    def appendFunc(self, data):
        #this will add a new data point to the list
        new_node = Node()
        curr = self.head #as there are no nodes the current node is the head node
        #interate over notes in the list until we find the next node of curr which is None
        #we then insert the new node at this new location
        while curr.next !=None:
            #traverse through the list
            curr = curr.next
        #once we are at the last node make the new node the next node of the current node
        curr.next = new_node
        #be sure to text the code at this stage
    
        

myLinkedList = LinkedList()
myLinkedList.appendFunc(5)
myLinkedList.appendFunc(22)
print(myLinkedList)
