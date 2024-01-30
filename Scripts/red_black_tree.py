class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.red = True


class RedBlack(object):
    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.root = self.nil

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.nil
        new_node.right = self.nil

        if self.root == self.nil:
            new_node.red = False
            self.root = new_node

        else:
            parent = None
            current = self.root
            while current != self.nil:
                parent = current
                if value < current.value:
                    current = current.left
                elif value > current.value:
                    current = current.right
                else:
                    break
            new_node.parent = parent
            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

            self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)

    def rotate_left(self, unbalanced):
        new_root = unbalanced.right
        unbalanced.right = new_root.left
        if new_root.left != self.nil:
            new_root.left.parent = unbalanced

        new_root.parent = unbalanced.parent
        if unbalanced.parent == None:
            self.root = new_root
        elif unbalanced == unbalanced.parent.left:
            unbalanced.parent.left = new_root
        else:
            unbalanced.parent.right = new_root
        new_root.left = unbalanced
        unbalanced.parent = new_root

    # rotate right at node x
    def rotate_right(self, unbalanced):
        new_root = unbalanced.left
        unbalanced.left = new_root.righunbalanced
        if new_root.right != self.nil:
            new_root.right.parent = unbalanced

        new_root.parent = unbalanced.parent
        if unbalanced.parent == None:
            self.root = new_root
        elif unbalanced == unbalanced.parent.right:
            unbalanced.parent.right = new_root
        else:
            unbalanced.parent.left = new_root
        new_root.right = unbalanced
        unbalanced.parent = new_root