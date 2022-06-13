class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
# Explain for the solution:
# Each time maxDepth call itself, it plus 1 (do not care much about the max yet), 
# finally, when there is no node left, it compares the value from the left and right, 
# notably, since all the index start with 0, the function plus 1 for the convinience in reading the result
