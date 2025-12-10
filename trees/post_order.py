class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")

root = TreeNode('B')
nodeA = TreeNode('A')
nodeB = TreeNode('U')
nodeC = TreeNode('T')
nodeD = TreeNode('I')
nodeE = TreeNode('S')
nodeF = TreeNode('T')
nodeG = TreeNode('A')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
postOrderTraversal(root)

