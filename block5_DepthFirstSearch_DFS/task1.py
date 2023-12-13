# 1. Implement a DFS traversal in a binary tree.

# In this implementation, the TreeNode class represents a node in the binary tree, and the dfs_traversal function performs 
# a pre-order DFS traversal. You can customize the traversal order (pre-order, in-order, or post-order) based on your requirements.

# The example usage demonstrates creating a sample binary tree and performing DFS traversal on it. 
# You can modify the structure of the binary tree or values to test with different scenarios. 
# The output will display the DFS traversal result.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_traversal(node):
    result = []
    if node:
        # Pre-order traversal (Root, Left, Right)
        result.append(node.value)
        result.extend(dfs_traversal(node.left))
        result.extend(dfs_traversal(node.right))
    return result

# Example usage:
# Constructing a sample binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

dfs_result = dfs_traversal(root)
print("DFS Traversal Result:", dfs_result)
