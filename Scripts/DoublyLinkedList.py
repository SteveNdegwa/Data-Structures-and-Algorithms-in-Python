class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        defaultNode = Node(value)
        self.head = defaultNode
        self.tail = defaultNode
        self.length = 1

    def append (self, value):
        newNode = Node(value)
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend (self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
        self.length += 1

    def pop(self):
        self.head = self.head.next
        self.head.previous = None
        self.length -= 1

    def shift(self):
        self.tail = self.tail.previous
        self.tail.next = None
        self.length -= 1

    def reverse(self):
        


    def print(self):
        currentNode = self.head
        for x in range(self.length):
            print(currentNode.value)
            currentNode = currentNode.next

list = DoublyLinkedList(4)
list.append(5)
list.append(6)
list.prepend(3)
list.pop()
list.shift()
list.print()
