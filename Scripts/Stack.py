class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return False
        removed_node = self.head
        self.head = self.head.next
        self.length -= 1
        removed_node.next = None
        return removed_node

    def get_size(self):
        return self.length

    def peek(self):
        if self.length > 0:
            return self.head.value

    def print_stack(self):
        if self.length > 0:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next


stack = Stack()
stack.prepend(1)
stack.prepend(2)
stack.prepend(3)
stack.prepend(4)
print(stack.peek())
print(stack.get_size())
stack.pop_first()
print(stack.get_size())
stack.print_stack()
