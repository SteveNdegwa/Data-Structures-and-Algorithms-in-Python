class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        # new_node = Node(value)
        self.first = None
        self.last = None
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue_random(self, number):
        # use list(str(number))
        res = [int(x) for x in str(number)]
        for x in range(len(res)):
            if x + 2 in range(len(res)):
                print(res[x: x+3])
                self.enqueue(max(res[x: x+3]))
                # res.pop(0)


my_que = Queue()
my_que.enqueue_random(78966745831)
my_que.print_queue()
# implement this on the assignment  as below //

# random = 78966745831
# final = []
# res = [int(x) for x in str(random)]
# for x in res:
#     result = res[:3]
#     final.enqueue(max(result))
#     res = del res[-1:]
#
#
# # print (res)
# result = res[:3]  # form the first three
# max(result)  # find the max in the three
# del res[-1:]  # remove the first
