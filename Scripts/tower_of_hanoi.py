class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Rod:
    def __init__(self, name):
        self.head = None
        self.tail = None
        self.name = name
        self.length = 0
        if name == "A":
            self.prepend("3")
            self.prepend("2")
            self.prepend("1")

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
        return removed_node.value

    def print_stack(self):
        if self.length > 0:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next


A = Rod("A")
B = Rod("B")
C = Rod("C")


def move_disks(source, destination):
    value = source.pop_first()
    destination.prepend(value)
    print("Disk " + value + " moved from rod " + source.name + " to rod " + destination.name)


move_disks(A, C)
move_disks(A, B)
move_disks(C, B)
move_disks(A, C)
move_disks(B, A)
move_disks(B, C)
move_disks(A, C)





