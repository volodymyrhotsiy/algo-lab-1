class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root) -> bool:
    def dfs(root):
        stack = [(root, False)]
        heights = {}

        while stack:
            node, height = stack.pop()
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
            abs(left[1] - right[1]) <= 1)   

        return [balanced, 1 + max(right[1], left[1])] 
    return dfs(root)[0]      


# recursion
class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    

# Test case 1: A balanced tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
assert isBalanced(root1) == True

# Test case 2: An unbalanced tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.right = TreeNode(5)
assert isBalanced(root2) == False

# Test case 3: An empty tree
assert isBalanced(None) == True

# Test case 4: A single node tree
root4 = TreeNode(1)
assert isBalanced(root4) == True

# Test case 5: A slightly unbalanced tree
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(3)
root5.left.left = TreeNode(4)
root5.left.left.left = TreeNode(5)
root5.left.left.left.left = TreeNode(6)
root5.right.left = TreeNode(7)
assert isBalanced(root5) == False

# Test case 6: A balanced tree using the class-based solution
solution = Solution()
assert solution.isBalanced(root1) == True

# Test case 7: An unbalanced tree using the class-based solution
assert solution.isBalanced(root2) == False

# Test case 8: An empty tree using the class-based solution
assert solution.isBalanced(None) == True

# Test case 9: A single node tree using the class-based solution
assert solution.isBalanced(root4) == True

# Test case 10: A slightly unbalanced tree using the class-based solution
assert solution.isBalanced(root5) == False
