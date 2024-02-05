class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class Avl_tree:
    def heightFactor(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.heightFactor(node.left) - self.heightFactor(node.right)

    def right_rotate(self, unbalanced_node):
        new_node = unbalanced_node.left
        temp2 = new_node.right

        new_node.right = unbalanced_node
        unbalanced_node.left = temp2

        unbalanced_node.height = 1 + max(self.heightFactor(unbalanced_node.left), self.heightFactor(unbalanced_node.right))
        new_node.height = 1 + max(self.heightFactor(new_node.left), self.heightFactor(new_node.right))
        return new_node

    def leftrotate(self, unbalanced_node):
        new_node = unbalanced_node.right
        temp2 = new_node.left

        new_node.left = unbalanced_node
        unbalanced_node.right = temp2

        unbalanced_node.height = 1 + max(self.heightFactor(unbalanced_node.left), self.heightFactor(unbalanced_node.right))
        new_node.height = 1 + max(self.heightFactor(new_node.left), self.heightFactor(new_node.right))
        return new_node

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.key:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        root.height = 1 + max(self.heightFactor(root.left), self.heightFactor(root.right))

        balance = self.getBalance(root)
        if balance > 1:
            if value < root.left.key:
                return self.right_rotate(root)
            else:




