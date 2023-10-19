class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if not tree or not node:
        return None

    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor

    while node.parent and node.parent.right == node:
        node = node.parent

    return node.parent

root = BinaryTree(10)
root.left = BinaryTree(5, BinaryTree(3), None , root)
node = BinaryTree(7, None, None, root.left)
root.left.right = node
root.right = BinaryTree(15, None, BinaryTree(20, BinaryTree(12)), root)
root.left.right.parent = root.left = root


node_to_find_successor_for = root.left.right  # Node with value 7
successor = find_successor(root, node_to_find_successor_for)
if successor:
    print("Successor:", successor.value)
else:
    print("No successor found.")
