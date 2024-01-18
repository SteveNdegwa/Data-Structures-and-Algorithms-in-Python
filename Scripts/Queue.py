class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        removed_node = self.head
        self.head = self.head.next
        self.length -= 1
        return removed_node

    def get(self, index):
        if index not in range(self.length) or self.is_empty():
            return None
        current_node = self.head
        for x in range(self.length):
            if x == index:
                return current_node
            current_node = current_node.next

    def update(self, index, new_value):
        if index not in range(self.length) or self.is_empty():
            return False
        node = self.get(index)
        node.value = new_value
        return True

    def insert(self, index, value):
        if index not in range(self.length) or self.is_empty():
            return False
        new_node = Node(value)
        previous_node = self.get(index-1)
        next_node = previous_node.next
        previous_node.next = new_node
        new_node.next = next_node
        self.length += 1
        return True

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def print_queue(self):
        if self.is_empty():
            return
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next


queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.print_queue()





