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
        new_node = Node(data)
        current = self.head #as there are no nodes the current node is the head node
        #interate over notes in the list until we find the next node of curr which is None
        #we then insert the new node at this new location
        while current.next != None:
            #traverse through the list
            current = current.next
        #once we are at the last node make the new node the next node of the current node
        current.next = new_node
        
    def display(self):
        #helper function to display the contents of the linked list
        visitedElements = [] # store elements in the list
        current = self.head # traverse the list starting with the head node
        while current.next !=None:
            current = current.next
            visitedElements.append(current.data)
        print(visitedElements)
 
        
        
    
        

myList = LinkedList()
myList.display()
myList.appendFunc(5)
myList.appendFunc(22)
myList.display()
