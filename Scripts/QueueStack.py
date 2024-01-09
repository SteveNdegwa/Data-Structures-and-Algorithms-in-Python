class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Queue:
    def __init__(self):
        self.head = None        
        self.tail = None        
        self.length = 0

    def queue(self, value):
        newNode = Node(value)
        if (self.length == 0):
            self.head = newNode
            self.tail = newNode

        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1 

     def dequeue(self):
             if(self.length == 0):
                return
             else:
                self.head = self.head.next
                self.head.previous = None
                self.length -= 1        

     def print(self):
        if(self.length > 0):
            currentNode = self.head
            for x in range(self.length):
                print(currentNode.value)
                currentNode = currentNode.next   
                   

class Stack:
      def __init__(self):
        self.head = None        
        self.tail = None        
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if (self.length == 0):
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

        self.length += 1 

     def pop(self):
             if(self.length == 0):
                return
             else:
                self.head = self.head.next
                self.head.previous = None
                self.length -= 1        

     def print(self):
        if(self.length > 0):
            currentNode = self.head
            for x in range(self.length):
                print(currentNode.value)
                currentNode = currentNode.next
                   


