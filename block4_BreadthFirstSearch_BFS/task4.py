# # 4. Write a program for level order traversal in a binary tree using BFS.
# In this implementation, the TreeNode class represents a node in the binary tree, 
# and the level_order_traversal function performs the level order traversal. The algorithm uses a queue to visit nodes level by level. 
# It starts with the root node, dequeues it, processes its value, and enqueues its children if they exist.

# The example usage demonstrates creating a sample binary tree and performing level order traversal on it. 
# You can modify the structure of the binary tree or values to test with different scenarios. 
# The output will display the level order traversal result.

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

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

level_order_result = level_order_traversal(root)
print("Level Order Traversal Result:", level_order_result)
