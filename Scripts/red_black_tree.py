class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.red = True


class RedBlack(object):
    def __init__(self):
        self.nil = Node(None)
        self.red = False
        self.root = self.nil

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.nil
        new_node.right = self.nil

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return

        new_node.parent = parent

        if not parent:
            new_node.red = False
            self.root = new_node
        elif value > parent.value:
            parent.right = new_node
        else:
            parent.left = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            # get the uncle of the new node
            if new_node.parent.parent.left == new_node.parent:
                uncle = new_node.parent.parent.right
            else:
                uncle = new_node.parent.parent.left

            # check if uncle is red
            if uncle.red:
                uncle.red = False
                new_node.parent.red = False
                if new_node.parent.parent != self.root:
                    new_node.parent.parent.red = True
                    new_node = new_node.parent

            # if uncle is black or nil
            else:
                # if parent is on left of grandparent
                if new_node.parent.parent.left == new_node.parent:
                    # left-right
                    if new_node.parent.right == new_node:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)

                # if parent is on right of grandparent
                else:
                    # right-left
                    if new_node.parent.left == new_node:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)

    def rotate_left(self, unbalanced):
        new_root = unbalanced.right
        new_root.parent = unbalanced.parent

        if not new_root.parent:
            self.root = new_root
        elif new_root.value < new_root.parent.value:
            new_root.parent.left = new_root
        else:
            new_root.parent.right = new_root

        unbalanced.right = new_root.left
        if new_root.left != self.nil:
            unbalanced.right.parent = unbalanced

        new_root.left = unbalanced
        unbalanced.parent = new_root

    def rotate_right(self, unbalanced):
        new_root = unbalanced.left
        new_root.parent = unbalanced.parent

        if not new_root.parent:
            self.root = new_root
        elif new_root.value < new_root.parent.value:
            new_root.parent.left = new_root
        else:
            new_root.parent.right = new_root

        unbalanced.left = new_root.right
        if new_root.right != self.nil:
            unbalanced.left.parent = unbalanced

        new_root.right = unbalanced
        unbalanced.parent = new_root

    def preorder(self, root):
        if not root:
            return
        print(f"value:{root.value}, red:{root.red}")
        self.preorder(root.left)
        self.preorder(root.right)


tree = RedBlack()
tree.insert(10)
tree.insert(18)
tree.insert(7)
tree.insert(15)
tree.insert(16)
tree.insert(30)
tree.insert(25)
tree.insert(40)
tree.insert(60)
tree.insert(2)
tree.insert(1)
tree.insert(70)
tree.preorder(tree.root)


