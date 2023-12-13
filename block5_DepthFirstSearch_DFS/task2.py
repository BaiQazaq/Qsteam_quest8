# 2. Write a program to find all root-to-leaf paths in a binary tree using DFS.

# In this implementation, the TreeNode class represents a node in the binary tree, and the all_paths_dfs function is 
# a recursive helper function that traverses the tree using DFS, building paths from the root to leaf nodes. 
# The find_all_paths function initializes the result list and starts the DFS traversal.

# The example usage demonstrates creating a sample binary tree and finding all root-to-leaf paths. 
# You can modify the structure of the binary tree or values to test with different scenarios. 
# The output will display all the root-to-leaf paths in the binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def all_paths_dfs(node, current_path, result):
    if not node:
        return

    current_path.append(node.value)

    if not node.left and not node.right:
        result.append(current_path.copy())  # Add a copy of the current path when a leaf node is reached

    all_paths_dfs(node.left, current_path, result)
    all_paths_dfs(node.right, current_path, result)

    current_path.pop()  # Backtrack

def find_all_paths(root):
    result = []
    all_paths_dfs(root, [], result)
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

paths = find_all_paths(root)
print("All Root-to-Leaf Paths:")
for path in paths:
    print(path)
