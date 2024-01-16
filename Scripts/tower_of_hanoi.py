class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Rod:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return
        removed_node = self.top
        self.top = self.top.next
        self.length -= 1
        removed_node.next = None
        return removed_node.value

    def print_stack(self):
        if self.length > 0:
            current_node = self.top
            while current_node:
                print(current_node.value)
                current_node = current_node.next


def move_disks_between_two_poles(src, dest, s, d):
    pole1_top_disk = src.pop()
    pole2_top_disk = dest.pop()

    # When pole 1 is empty
    if pole1_top_disk is None:
        src.push(pole2_top_disk)
        print(f"Move the disk '{str(pole2_top_disk)}' from '{d}' to '{s}'")
        return

    # When pole2 pole is empty
    elif pole2_top_disk is None:
        dest.push(pole1_top_disk)
        print(f"Move the disk '{str(pole1_top_disk)}' from '{s}' to '{d}'")
        return

    # When top disk of pole1 > top disk of pole2
    elif pole1_top_disk > pole2_top_disk:
        src.push(pole1_top_disk)
        src.push(pole2_top_disk)
        print(f"Move the disk '{str(pole2_top_disk)}' from '{d}' to '{s}'")
        return

    # When top disk of pole1 < top disk of pole2
    else:
        dest.push(pole2_top_disk)
        dest.push(pole1_top_disk)
        print(f"Move the disk '{str(pole1_top_disk)}' from '{s}' to '{d}'")


def initialize(num_of_disks, src, aux, dest):
    total_num_of_moves = pow(2, num_of_disks) - 1

    # If number of disks is even, then interchange
    # destination pole and auxiliary pole

    # if num_of_disks % 2 == 0:
    #     aux, dest = dest, aux

    for j in range(num_of_disks, 0, -1):
        src.push(j)

    return total_num_of_moves


def iterate(i, total_no_of_moves, src, aux, dest):
    if i in range(1, total_no_of_moves + 1):
        if i % 3 == 1:
            move_disks_between_two_poles(src, dest, 'S', 'D')
        elif i % 3 == 2:
            move_disks_between_two_poles(src, aux, 'S', 'A')
        else:
            move_disks_between_two_poles(aux, dest, 'A', 'D')
        i += 1


S = Rod()
A = Rod()
D = Rod()

total_no_of_moves = initialize(4, S, A, D)


# run the nth move
def run_move(n):
    return iterate(n, total_no_of_moves, S, A, D)


# run n moves
def run(n):
    for i in range(1, n + 1):
        iterate(i, total_no_of_moves, S, A, D)


run_move(1)
run_move(2)
run_move(3)
run_move(4)
