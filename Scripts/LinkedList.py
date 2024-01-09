# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        defaultNode = Node(value)
        self.head = defaultNode
        self.tail = defaultNode
        self.length = 1

    def append (self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length = self.length + 1

    def prepend (self, value):
       newNode = Node(value)
       newNode.next = self.head
       self.head = newNode
       self.length = self.length + 1

    def shift(self):
        currentNode = self.head
        for x in range(self.length):
            if(currentNode.next == self.tail):
                currentNode.next = None
                self.length = self.length - 1
                return
            currentNode = currentNode.next

    def pop(self):
        self.head = self.head.next
        self.length = self.length - 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    def print(self):
        currentNode = self.head
        for x in range(self.length):
            print(currentNode.value)
            currentNode = currentNode.next




list = LinkedList(4)
list.append(5)
list.append(6)
list.reverse()
list.print()
