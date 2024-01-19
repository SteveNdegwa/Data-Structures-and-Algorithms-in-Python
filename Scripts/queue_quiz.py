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

    def print_queue(self):
        if self.is_empty():
            return
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def largest_numbers(self, numbers):
        for i in range(len(numbers)):
            if i + 2 in range(len(numbers)):
                largest = numbers[i]
                if numbers[i+1] > numbers[i]:
                    largest = numbers[i+1]
                if numbers[i+2] > largest:
                    largest = numbers[i+2]
                # largest = max(numbers[i: i + 3])
                self.enqueue(largest)


queue = Queue()
numbers = [7, 8, 9, 6, 7, 4, 5, 8, 3, 1]
# numbers = [4, 6, 7, 1, 2, 4, 5, 8, 9, 6]
queue.largest_numbers(numbers)
queue.print_queue()

