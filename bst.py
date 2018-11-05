class BinarySearchTree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, root, child):
        if root.value > child.value:
            if root.left == None:
                root.left = child
            else:
                root.insert(root.left, child)
        elif root.value <= child.value:
            if root.right == None:
                root.right = child
            else:
                root.insert(root.right, child)
