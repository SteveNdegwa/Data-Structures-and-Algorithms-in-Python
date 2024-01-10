class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length > 0:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return True
        return False

    def pop(self):
        if self.length > 0:
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return True
        return False

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


linked_list = DoublyLinkedList()
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.prepend(3)
linked_list.pop_first()
linked_list.print()
