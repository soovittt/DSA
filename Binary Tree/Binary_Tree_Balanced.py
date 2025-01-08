'''
Given a binary tree, find if it is height balanced or not.  A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 
'''


class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalancedOptimised(self,root):
        if root is None:
            p = [True,0]
            return p
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        leftAns = left[0]
        rightAns = right[0]
        diff = abs(left[1]-right[1]) <=1
        ans = [0,0]
        ans[1] = max(left[1],right[1])+1
        if leftAns and rightAns and diff:
            ans[0] = True
        else:
            ans[0] = False
        return ans
    def isBalanced(self,root):
        return self.isBalancedOptimised(root)[0]

