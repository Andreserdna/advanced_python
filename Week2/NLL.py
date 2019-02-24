class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    #return the head element in the list
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    #return the last element in the list
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element
    # add an element to the beggining of the list
    def addFirst(self,e):
        newNode = Node(e) #create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # increases the list size

        if self.__tail == None: #the new node is the only node in the list
            self.__tail = self.__head
    #add an element to the end of the list
    def addLast(self,e):
        newNode = Node(e) #create a new node for e
        
        if self.__tail == None:
            self.__head = self.__tail = newNode #the only node in the list
        else:
            self.__tail.next = newNode # link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
        self.__size += 1 #increase the size

