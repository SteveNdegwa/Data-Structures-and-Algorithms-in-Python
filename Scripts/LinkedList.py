# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self):
        if(self.length > 0):
            currentnode = self.head
            for _ in range(self.length):
                if (currentnode.next == self.tail):
                    currentnode.next = None
                    self.tail = currentnode
                    self.length -= 1
                    return True
                currentnode = currentnode.next
        return False

    def popFirst(self):
        if (self.length > 0):
            self.head = self.head.next
            self.length -= 1
            return True
        return False

    def get (self, index):
        if(index >=0 and index in range(self.length)):
            currentNode = self.head
            for x in range(self.length):
                if(index == x):
                    return currentNode
                currentNode = currentNode.next
        return None

    def changeValue(self, index, newValue):
        node = self.get(index)
        if(node != None):
            node.value = newValue

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
        if(self.length > 0):
            currentNode = self.head
            for _ in range(self.length):
                print(currentNode.value)
                currentNode = currentNode.next



linked_list = LinkedList()
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.prepend(3)
linked_list.print()

