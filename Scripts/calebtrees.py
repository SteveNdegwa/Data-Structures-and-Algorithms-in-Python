class Node:
    def __init__(self ,value):
        self.value = value
        self.left = None
        self. right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:

            if new_node.value == temp.value:
                 return False

            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
                if value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
                else:
                    return  True
        return False
    def bfs(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []
        def tranferse (current_node)
            results.append(current_node)



    # def delete(self, value):
    #     if self.root is None:
    #         print('tree is empty')
    #         return
    #     temp = self.root
    #     i`f value < temp.value:
    #         if temp.left:
    #             temp.left = temp.left.del(value)
    #         else:
    #             print("Given node not found")
    #     elif value > temp.value:
    #         if temp.right:
    #             temp.right = temp.right.delete(value)
    #         else:
    #             print("Given node not found")
    #     else:
    #         if temp.left is None:
    #             temp = temp.right
    #             self.root = None
    #             return temp
    #
    #         else:
    #             if temp.right is None:
    #                 temp = temp.left
    #                 self.root = None
    #                 return temp
    #             Node = temp.right
    #             while temp.left:
    #                 Node = temp.left
    #             self.key = self.root.value
    #             temp.right = temp.right.del(value)
    #             return temp.value`




# deletion
# inorder
# postorder and level order






my_tree = BinarySearchTree()
my_tree.insert(20)
my_tree.insert(14)
my_tree.insert(32)
my_tree.insert(12)
my_tree.insert(12)
my_tree.insert(6)

print(my_tree.bfs())




