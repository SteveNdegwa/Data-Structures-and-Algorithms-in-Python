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

    def append(self, value):  # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):  # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):  # O(n)
        if self.length > 0:
            current_node = self.head
            for _ in range(self.length):
                if current_node.next == self.tail:
                    current_node.next = None
                    self.tail = current_node
                    self.length -= 1
                    return True
                current_node = current_node.next
        return False

    def pop_first(self):  # O(1)
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1
            return True
        return False

    def get(self, index):  # O(n)
        if index >= 0 and index in range(self.length):
            current_node = self.head
            for x in range(self.length):
                if index == x:
                    return current_node
                current_node = current_node.next
        return False

    def change_value(self, index, new_value):  # O(n)
        node = self.get(index)  # O(n)
        if node:
            node.value = new_value

    def remove(self, index):  # O(n)
        node = self.get(index)
        previous_node = self.get(index-1)
        previous_node.next = node.next
        node.next = None
        self.length -= 1

    def reverse(self):  # O(n)
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

    def print(self):  # O(n)
        if self.length > 0:
            current_node = self.head
            for _ in range(self.length):
                print(current_node.value)
                current_node = current_node.next


linked_list = LinkedList()
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.prepend(3)
linked_list.reverse()
print(linked_list.get(2).value)
linked_list.print()

