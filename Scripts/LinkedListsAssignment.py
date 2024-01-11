class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.bucket_1 = list()
        self.bucket_2 = list()
        self.bucket_3 = list()

    def append(self, value):  # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def populate(self, n):
        for x in range(n):
            x += 1
            self.append(x)

    def pop(self):  # O(n)
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def pop_first(self):  # O(1)
        if self.length > 0:
            removed_value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return removed_value
        return None

    def empty_list(self):
        pop_first = True
        bucket = 1
        for _ in range(self.length):
            if pop_first:
                value = self.pop_first()
                pop_first = False
            else:
                pop_first = True
                value = self.pop()
            if bucket > 3:
                bucket = 1
            if bucket == 1:
                self.bucket_1.append(value)
            if bucket == 2:
                self.bucket_2.append(value)
            if bucket == 3:
                self.bucket_3.append(value)
            bucket += 1
        print(self.bucket_1)
        print(self.bucket_2)
        print(self.bucket_3)

    def print(self):  # O(n)
        if self.length > 0:
            current_node = self.head
            for _ in range(self.length):
                print(current_node.value)
                current_node = current_node.next


linked_list = LinkedList()
linked_list.populate(100)
linked_list.print()
linked_list.empty_list()
linked_list.print()
