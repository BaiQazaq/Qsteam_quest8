# 1. Implement a BFS traversal in a binary tree.

# In this implementation, the TreeNode class represents a node in the binary tree, and the bfs_traversal function performs the BFS traversal. 
# The algorithm uses a queue to visit nodes level by level. It starts with the root node, dequeues it, 
# processes its value, and enqueues its children if they exist.

# The example usage demonstrates creating a sample binary tree and performing BFS traversal on it. 
# You can modify the structure of the binary tree or values to test with different scenarios. 
# The output will display the BFS traversal result.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)
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
#        / \
#       4   5
#          /
#         6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(6)

bfs_result = bfs_traversal(root)
print("BFS Traversal Result:", bfs_result)

# print(root.value)
# print(root.left.value)
# print(root.right.value)
# print(root.right.left.value)
# print(root.right.right.value)
# print(root.right.right.left.value)

