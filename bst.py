class BinarySearchTree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if self.value > child.value:
            if self.left == None:
                self.left = child
            else:
                self.left.insert(child)
        else:
            if self.right == None:
                self.right = child
            else:
                self.right.insert(child)

    def find(self, searchee):
        if searchee == self.value:
            return True
        if self.value > searchee:
            if self.left is None:
                return False
            return self.left.find(searchee)
        else:
            if self.right is None:
                return False
            return self.right.find(searchee)

    def in_order_traversal(self, callback):
        if self.left is not None:
            self.left.in_order_traversal(callback)
        callback(self.value)
        if self.right is not None:
            self.right.in_order_traversal(callback)

    def pre_order_traversal(self, callback):
        callback(self.value)
        if self.left is not None:
            self.left.pre_order_traversal(callback)
        if self.right is not None:
            self.right.pre_order_traversal(callback)

    def post_order_traversal(self, callback):
        if self.left is not None:
            self.left.post_order_traversal(callback)
        if self.right is not None:
            self.right.post_order_traversal(callback)
        callback(self.value)

    def delete(self, deletee):
        if self.right is not None and self.right.value == deletee:
            if self.right.left is None:
                self.right = self.right.right
            elif self.right.right is None:
                self.right = self.right.left
            else:
                successor = self.right.right
                while successor.left is not None:
                    successor = successor.left
                self.right.delete(successor.value)
                self.right.value = successor.value
        elif self.left is not None and self.left.value == deletee:
            if self.left.right is None:
                self.left = self.left.left
            elif self.left.left is None:
                self.left = self.left.right
            else:
                successor = self.left.left
                while successor.right is not None:
                    successor = successor.right
                self.left.delete(successor.value)
                self.left.value = successor.value
        else:
            if deletee > self.value:
                if self.right is not None:
                    self.right.delete(deletee)
            else:
                if self.left is not None:
                    self.left.delete(deletee)
