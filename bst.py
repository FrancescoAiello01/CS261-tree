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
