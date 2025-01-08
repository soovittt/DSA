'''
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. The diagram below shows two trees each with diameter nine, the leaves that form the ends of the longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes). 
'''
class Solution:
    
    #Function to return the diameter of a Binary Tree.

    def diameterOptimised(self,root):
        pair = []
        if root is None:
            return []
        left = self.diameterOptimised(root.left)
        right = self.diameterOptimised(root.right)
        op1,op2,op3 = left[0],right[0],left[1] + right[1] + 1
        ans = []
        ans[0] , ans[1] = max(op1,op2,op3) , max(left[1],right[1]) + 1
        return ans
        



    def diameterNormal(self,root):
        if root is None:
            return 0
        op1 = self.diameterNormal(root.left)
        op2 = self.diameterNormal(root.right)
        op3 = self.height(root.left) + self.height(root.right) + 1
        return max(op1,op2,op3)



    def diameter(self,root):
        return self.diameterOptimised(root)