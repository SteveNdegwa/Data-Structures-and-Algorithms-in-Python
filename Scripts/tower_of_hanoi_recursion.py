class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, name):
        self.head = None
        self.tail = None
        self.name = name
        self.length = 0
        if name == "A":
            self.push(3)
            self.push(2)
            self.push(1)

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
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


def move_nodes(n, src, dest, aux):
    if n == 1:
        # dest.push(src.pop())
        return print(f"Disk {n} moved from {src.name} to {dest.name}")
    move_nodes(n-1, src, aux, dest)
    # aux.push(src.pop())
    print(f"Disk {n} moved from {src.name} to {aux.name}")
    move_nodes(n-1, aux, dest, src)


A = Stack("A")
B = Stack("B")
C = Stack("C")

move_nodes(3, A, C, B)


