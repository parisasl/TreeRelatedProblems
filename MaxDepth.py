# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        Depthleft = Solution().maxDepth(root.left)
        Depthright = Solution().maxDepth(root.right)
        MaxD = max(Depthleft,Depthright)+1
        return MaxD
root = TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))
print(Solution().maxDepth(root))