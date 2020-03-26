class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

def preorderRecursive(root, result):
    if not root:
        return

    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)

def inorderRecursive(root, result):
    if not root:
        return

    preorderRecursive(root.left, result)
    result.append(root.data)
    preorderRecursive(root.right, result)

def postorderRecursive(root, result):
    if not root:
        return

    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)
    result.append(root.data)
