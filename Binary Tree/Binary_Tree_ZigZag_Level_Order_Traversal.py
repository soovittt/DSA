class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)
        leftToRight = True 
        while len(queue)!=0:
            sizeQ = len(queue)
            row = []
            for i in range(0,sizeQ):
                node = queue.pop(0)
                index = i if leftToRight else (sizeQ-1-i)
                row[index] = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            leftToRight != leftToRight
            result.append(row)
        return result



        