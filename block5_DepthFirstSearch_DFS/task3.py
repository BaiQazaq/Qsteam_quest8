# # 3. Implement a DFS solution to check if a tree is a valid binary search tree.

# In this implementation, the TreeNode class represents a node in the binary tree, and the is_valid_bst function is 
# a recursive DFS function that checks whether the tree is a valid BST by comparing the values during an in-order traversal. 
# The min_val and max_val parameters are used to track the valid range for each node.

# The example usage demonstrates creating a valid BST and an invalid BST and checking their validity using the is_valid_bst function. 
# You can modify the structure of the trees to test with different scenarios. 
# The output will indicate whether the given tree is a valid BST or not.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True

    if not min_val < node.value < max_val:
        return False

    return (
        is_valid_bst(node.left, min_val, node.value) and
        is_valid_bst(node.right, node.value, max_val)
    )

# Example usage:
# Constructing a valid Binary Search Tree (BST):
#       2
#      / \
#     1   3

valid_bst_root = TreeNode(2)
valid_bst_root.left = TreeNode(1)
valid_bst_root.right = TreeNode(3)

print("Is the tree a valid BST?", is_valid_bst(valid_bst_root))

# Constructing an invalid Binary Search Tree (BST):
#       5
#      / \
#     1   4
#        / \
#       3   6

invalid_bst_root = TreeNode(5)
invalid_bst_root.left = TreeNode(1)
invalid_bst_root.right = TreeNode(4)
invalid_bst_root.right.left = TreeNode(3)
invalid_bst_root.right.right = TreeNode(6)

print("Is the tree a valid BST?", is_valid_bst(invalid_bst_root))
