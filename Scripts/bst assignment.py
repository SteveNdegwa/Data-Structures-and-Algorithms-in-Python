class Node():
    def __init__(self ,value):
        self.value = value
        self.left = None
        self. right = None
class Binary_search():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value > temp.value:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left


    def Bfs(self):
        current_node = self.root
        temp_list = []
        results = []
        temp_list.append(current_node)
        while len(temp_list) > 0:
            current_node = temp_list.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                temp_list.append(current_node.left)
            if current_node.right is not None:
                temp_list.append(current_node.right)
        return results

my_tree = Binary_search()
my_tree.insert(20)
my_tree.insert(14)
my_tree.insert(32)
my_tree.insert(12)
my_tree.insert(12)
my_tree.insert(6)

print(my_tree.Bfs())
