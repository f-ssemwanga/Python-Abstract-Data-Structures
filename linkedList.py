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
        #interate over nodes in the list until we find the next node of curr which is None
        #we then insert the new node at this new location
        while current.next != None:
            #traverse through the list
            current = current.next
        #once we are at the last node make the new node the next node of the current node
        current.next = new_node
        
    def display(self):
        #helper function to display the contents of the linked list
        listElements = [] # store elements in the list
        current = self.head # traverse the list starting with the head node
        while current.next !=None:
            current = current.next
            listElements.append(current.data)
        print(listElements)
    def length(self):
        #useful function for finding how large the data structure is
        current = self.head # starting at the node pointer
        total = 0 # counts nodes encountered
        while current.next != None:
            total +=1
            current = current.next
        return total
    def getElement(self, index):
        #extractor function for pulling out data items
        #take index to extract from as an argument
        #it is worth checking first whether the passed index is not out of range
        if index >= self.length():
            print("Error: 'Given index was out of range'")
            return None
        current_index = 0
        current_node = self.head
        while True:
            # as by now we are sure the index is in range
            #This loop is guaranteed to terminate
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index +=1
    def eraseItem(self):
        index = int(input('Enter the index of the item to remove: '))
        #check of given index is valid
        if index >= self.length() or index <0:
            print('Error: Given index is out of range')
            return None
        #if item to be removed is the head node
        elif index ==0:
            self.head = self.head.next
        else:
            previous = None
            current_node =self.head
            i =0 #starting index for iterating over the list
            #traverse the list to find node at given index
            while i <index:
                previous = current_node
                current_node = current_node.next
                i +=1
            #update the pointers to remove the node at the given index
            previous.next = current_node.next
            current_node.next = None   
                
    
myList = LinkedList()
myList.display()
myList.appendFunc(5)
myList.appendFunc(22)
myList.appendFunc(28)
myList.display()
print(f'linked list size is {myList.length()}')
index = int(input('Enter index of element to find: '))
print(f' The element at index {index} is {myList.getElement(index)}')
myList.eraseItem()
myList.display()

