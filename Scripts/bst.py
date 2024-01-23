class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.root = new_node
            return
        return self.insert_node(self.root, new_node)

    def insert_node(self, root, new_node):
        while True:
            if new_node.value < root.value:
                if root.left is None:
                    root.left = new_node
                    return
                root = root.left
            else:
                if root.right is None:
                    root.right = new_node
                    return
                root = root.right

        # if new_node.value < root.value:
        #     if root.left is None:
        #         root.left = new_node
        #         return
        #     self.insert_node(root.left, new_node)
        # else:
        #     if root.right is None:
        #         root.right = new_node
        #         return
        #     self.insert_node(root.left, new_node)

    def search(self, root, value):
        current_node = root
        while current_node:
            if current_node.value == value:
                return current_node
            if value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None

        # if not root:
        #     return None
        # elif root.value == value:
        #     return root.value
        # elif value < root.value:
        #     return self.search(root.left, value)
        # else:
        #     return self.search(root.right, value)

    def min(self, root):
        if self.is_empty():
            return None
        current_node = root
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def max(self, root):
        if self.is_empty():
            return None
        current_node = root
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    def delete(self, value):
        self.root = self.delete_node(self.root, value)

    def delete_node(self, root, value):
        if not root:
            return root
        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if (not root.left) and (not root.right):
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.value = self.min(root.right)
            root.right = self.delete_node(root.right, root.value)
        return root

    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value)

    def levelorder(self):
        queue = list()
        queue.append(self.root)
        while queue:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def join_bst(self, root):
        if not root:
            return
        self.join_bst(root.left)
        self.insert(root.value)
        self.join_bst(root.right)


bst = BST()
bst.insert(16)
bst.insert(10)
bst.insert(6)
bst.insert(12)
bst.insert(24)
bst.insert(20)
bst.insert(28)
bst2 = BST()
bst2.insert(25)
bst2.insert(13)
bst2.insert(8)
bst2.insert(19)
bst2.insert(29)
bst2.insert(26)
bst2.insert(32)
print("BST 1")
bst.preorder(bst.root)
print("BST 2")
bst.preorder(bst.root)
bst.join_bst(bst2.root)
print("BST 1 after joining")
bst.levelorder()
# print(bst.search(bst.root, 2))
# print(bst.min(bst.root))
# root = bst.search(bst.root, 6)
# print(bst.max(root))
