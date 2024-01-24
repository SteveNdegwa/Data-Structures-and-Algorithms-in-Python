    class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        item_to_remove = self.head
        self.head = self.head.next
        self.head.previous = None
        item_to_remove.next = None
        self.length -= 1

    def get(self, index):
        if index >= 0 and index in range(self.length):
            current_node = self.head
            for x in range(self.length):
                if x == index:
                    return current_node
                current_node = current_node.next
        return False

    def change_value(self, index, new_value):
        node = self.get(index)  # O(n)
        if node:
            node.value = new_value

    def remove(self, index):  # O(n)
        if self.length > 0:
            node = self.get(index)
            previous_node = node.previous
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node
            node.next = None
            node.previous = None
            self.length -= 1
            return True
        return False

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            temp.previous = after
            before = temp
            temp = after

    def print(self):
        if self.length > 0:
            current_node = self.head
            for _ in range(self.length):
                print(current_node.value)
                current_node = current_node.next


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        item_to_remove = self.head
        self.head = self.head.next
        self.head.previous = None
        item_to_remove.next = None
        self.length -= 1

    def get(self, index):
        if index >= 0 and index in range(self.length):
            current_node = self.head
            for x in range(self.length):
                if x == index:
                    return current_node
                current_node = current_node.next
        return False

    def change_value(self, index, new_value):
        node = self.get(index)  # O(n)
        if node:
            node.value = new_value

    def remove(self, index):  # O(n)
        if self.length > 0:
            node = self.get(index)
            previous_node = node.previous
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node
            node.next = None
            node.previous = None
            self.length -= 1
            return True
        return False

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            temp.previous = after
            before = temp
            temp = after

    def print(self):
        if self.length > 0:
            current_node = self.head
            for _ in range(self.length):
                print(current_node.value)
                current_node = current_node.next
