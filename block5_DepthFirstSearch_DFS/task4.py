# 4. Write a program to find the diameter of a tree using DFS.

# In this implementation, the TreeNode class represents a node in the binary tree, and the tree_diameter function 
# is a wrapper function that initializes the diameter variable and calls the recursive DFS function dfs. 
# The dfs function calculates the height of the left and right subtrees and updates the diameter if a longer path is found.

# The example usage demonstrates creating a sample binary tree and finding its diameter using the tree_diameter function. 
# You can modify the structure of the binary tree to test with different scenarios. The output will display the diameter of the tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_diameter(root):
    def dfs(node):
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # Update the diameter during the DFS traversal
        nonlocal diameter
        diameter = max(diameter, left_height + right_height)

        # Return the height of the subtree rooted at 'node'
        return 1 + max(left_height, right_height)

    diameter = 0
    dfs(root)
    return diameter

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

diameter = tree_diameter(root)
print("Diameter of the tree:", diameter)
