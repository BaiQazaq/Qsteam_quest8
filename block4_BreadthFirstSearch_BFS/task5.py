# 5. Implement a method to find the maximum width of a binary tree using BFS.

# In this implementation, the TreeNode class represents a node in the binary tree, 
# and the max_width_bfs function performs the BFS traversal while keeping track of the position of each node. 
# The width of each level is calculated, and the maximum width is updated accordingly.

# The example usage demonstrates creating a sample binary tree and finding its maximum width. 
# You can modify the structure of the binary tree to test with different scenarios. 
# The output will display the maximum width of the binary tree.

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_width_bfs(root):
    if not root:
        return 0

    max_width = 0
    queue = deque([(root, 0)])  # (node, position)

    while queue:
        level_size = len(queue)
        _, start_position = queue[0]

        for i in range(level_size):
            current_node, position = queue.popleft()

            if current_node.left:
                queue.append((current_node.left, 2 * position))

            if current_node.right:
                queue.append((current_node.right, 2 * position + 1))

        max_width = max(max_width, position - start_position + 1)

    return max_width

# Example usage:
# Constructing a sample binary tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   8
#  /
# 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(6)

width = max_width_bfs(root)
print("Maximum Width of the Binary Tree:", width)
