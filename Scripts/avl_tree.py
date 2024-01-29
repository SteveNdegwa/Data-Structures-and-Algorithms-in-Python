class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL(object):
    def __init__(self):
        self.root = None

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self.root = self.insert_node(self.root, value)

    def insert_node(self, root, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # left left
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # left right
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # right right
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # right left
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, unbalanced_node):
        new_root = unbalanced_node.right
        unbalanced_node.right = new_root.left
        new_root.left = unbalanced_node

        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        unbalanced_node.height = 1 + max(self.get_height(unbalanced_node.left), self.get_height(unbalanced_node.right))

        return new_root

    def right_rotate(self, unbalanced_node):
        new_root = unbalanced_node.left
        unbalanced_node.left = new_root.right
        new_root.right = unbalanced_node

        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        unbalanced_node.height = 1 + max(self.get_height(unbalanced_node.left), self.get_height(unbalanced_node.right))

        return new_root

    def preorder(self, root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return
        self.preorder(root.left)
        print(root.value)
        self.preorder(root.right)



avl = AVL()
avl.insert(34)
avl.insert(26)
avl.insert(44)
avl.insert(13)
avl.insert(29)
avl.insert(49)
avl.insert(10)
avl.insert(7)
avl.insert(9)
avl.preorder(avl.root)