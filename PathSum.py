# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if not root.right and not root.left and root.val == targetSum :
            return True
        targetSum -= root.val
        
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
    
root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7,None,None),TreeNode(2,None,None)),None),TreeNode(8,TreeNode(13,None,None),TreeNode(4,None,TreeNode(1,None,None))))
targetsum = 22
print(Solution().hasPathSum(root,targetsum))