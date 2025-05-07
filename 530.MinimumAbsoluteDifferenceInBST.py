# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Initialize previous node as None and minimum difference as infinity
        self.prev = None
        self.min_diff = float('inf')
        
        # Define the in-order traversal function
        def in_order_traverse(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order_traverse(node.left)
            
            # Process the current node
            if self.prev is not None:
                # Calculate the absolute difference with the previous node
                self.min_diff = min(self.min_diff, node.val - self.prev.val)
            
            # Update previous node to current node
            self.prev = node
            
            # Traverse the right subtree
            in_order_traverse(node.right)
        
        # Start the in-order traversal
        in_order_traverse(root)
        
        # Return the minimum difference found
        return self.min_diff

#this is so long, why it is in easy level...
