class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
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
            self.tail = new_node
        self.length += 1

    def dequeue(self, stack):
        if self.length == 0:
            return None
        removed_node = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        stack.prepend(removed_node.value)

    def initialize(self, values):
        for value in values:
            self.enqueue(value)

    def print_queue(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next


class Stack(object):
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self, queue):
        if self.length == 0:
            return None
        removed_node = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.top = None
            self.bottom = None
        queue.enqueue(removed_node.value)

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.value)
            current_node = current_node.next


def print_both(queue, stack):
    print("Queue:")
    queue.print_queue()
    print("Stack:")
    stack.print_stack()
    print(" ")


queue = Queue()
stack = Stack()
queue.initialize([2, 3, 4, 5])
print_both(queue, stack)
queue.dequeue(stack)
print_both(queue, stack)
stack.pop(queue)
print_both(queue, stack)

