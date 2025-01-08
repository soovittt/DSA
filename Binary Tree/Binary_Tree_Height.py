class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to find the height of a binary tree.
    
    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        ans = max(left,right) + 1
        return ans