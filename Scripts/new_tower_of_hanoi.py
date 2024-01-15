class TowerOfHanoi:
    def __init__(self):
        self.tower_a = []
        self.tower_b = []
        self.tower_c = []
        self.move_stack = []

    # def move(self, source, target):
    #     if source and (not target or source[-1] < target[-1]):
    #         target.append(source.pop())
    #         self.move_stack.append((source, target))
    #     elif target and (not source or target[-1] < source[-1]):
    #         source.append(target.pop())
    #         self.move_stack.append((target, source))
    # 
    # def solve(self):
    #     self.move_stack.append((self.tower_a, self.tower_b))
    #     while self.move_stack:
    #         source, target = self.move_stack.pop()
    #         print(source, target)
    #         self.move(source, target)
    # 
    # def move_right(self, source, destination, using):
    #     if source:
    #         if not destination or (destination[-1] > source[-1]):
    #             destination.append(source.pop())
    #         elif not using or (using[-1] > source[-1]):
    #             using.append(source.pop())


def move_disks_between_two_poles(src, dest, s, d):
    pole1_top_disk = src.pop()
    pole2_top_disk = dest.pop()

    # When pole 1 is empty
    if pole1_top_disk is None:
        src.push(pole2_top_disk)
        print(f"Move the disk from '{s}' to '{d}'")
        return

    # When pole2 pole is empty
    elif pole2_top_disk is None:
        dest.push(pole1_top_disk)
        print(f"Move the disk from '{s}' to '{d}'")
        return

    # When top disk of pole1 > top disk of pole2
    elif pole1_top_disk > pole2_top_disk:
        src.push(pole1_top_disk)
        print(f"Move the disk from '{s}' to '{d}'")
        return

    # When top disk of pole1 < top disk of pole2
    else:
        dest.push(pole2_top_disk)
        print(f"Move the disk from '{s}' to '{d}'")


def to_iterative(num_of_disks, src, aux, dest):
    total_num_of_moves = pow(2, num_of_disks) - 1

    # If number of disks is even, then interchange
    # destination pole and auxiliary pole
    if num_of_disks % 2 == 0:
        aux, dest = dest, aux

    # Larger disks will be pushed first
    for i in range(num_of_disks, 0, -1):
        src.append(i)

    for i in range(1, total_num_of_moves + 1):
        if i % 3 == 1:
            move_disks_between_two_poles(src, dest, 'S', 'D')
        elif i % 3 == 2:
            move_disks_between_two_poles(src, aux, 'S', 'A')
        else:
            move_disks_between_two_poles(aux, dest, 'A', 'D')


tower_of_hanoi = TowerOfHanoi()
to_iterative(3, tower_of_hanoi.tower_a, tower_of_hanoi.tower_b, tower_of_hanoi.tower_c)
