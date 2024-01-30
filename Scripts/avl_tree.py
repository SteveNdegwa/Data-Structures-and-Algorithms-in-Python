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

    def min(self, root):
        if not self.root:
            return None
        current_node = root
        while root.left:
            current_node = current_node.left
        return current_node.value

    def max(self, root):
        if not self.root:
            return None
        current_node = root
        while root.right:
            current_node = current_node.right
        return current_node.value

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self.root = self.insert_node(self.root, value)

    def insert_node(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        elif value > root.value:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # left-left
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # left-right
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # right-right
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # right-left
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, value):
        if not self.root:
            return None
        self.root = self.delete_node(self.root, value)

    def delete_node(self, root, value):
        if not root:
            return root
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        else:
            if (not root.left) and (not root.right):
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.value = self.min(root.right)
            root.right = self.delete_node(root.right, root.value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # left-left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # left-right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # right-right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # right-left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, unbalanced):
        new_root = unbalanced.right
        unbalanced.right = new_root.left
        new_root.left = unbalanced

        unbalanced.height = 1 + max(self.get_height(unbalanced.left), self.get_height(unbalanced.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def right_rotate(self, unbalanced):
        new_root = unbalanced.left
        unbalanced.left = new_root.right
        new_root.right = unbalanced

        unbalanced.height = 1 + max(self.get_height(unbalanced.left), self.get_height(unbalanced.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def preorder(self, root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
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
print()
avl.delete(34)
avl.preorder(avl.root)
