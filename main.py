from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # Initialize the queue with the root node and its depth.
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if this is a leaf node.
            if not node.left and not node.right:
                return depth
            
            # Add child nodes to the queue with incremented depth.
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
