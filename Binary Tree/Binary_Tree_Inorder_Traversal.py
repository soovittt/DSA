'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversalRecursive(self,root,sol):
        if(root is None):
            return
        self.inorderTraversalRecursive(root.left,sol)
        sol.append(root.val)
        self.inorderTraversalRecursive(root.right,sol)

    def inorderTraversal(self, root):
        sol = []
        self.inorderTraversalRecursive(root,sol)
        return sol

solution = Solution()
solution.inorderTraversal([1,None,2,3])
        
