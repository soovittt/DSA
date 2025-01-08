class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]
    i = 1

    while i < len(nums):
        node = queue.pop(0)

        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)

        i += 1

    return root

# Example usage:
nums = [2,None,3,None,4,None,5,None,6]
root = buildTree(nums)



from collections import deque
def zigzagLevelOrder(root):
    result = []
    
    if not root:
        return result
    
    queue = deque([root])
    reverse_order = False

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            if reverse_order:
                # Append the node values in reverse order
                node = queue.pop()
                level_values.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            else:
                # Append the node values in normal order
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        result.append(level_values)
        reverse_order = not reverse_order

    return result


            

    

# print(zigzagLevelOrder(root))


def maxDepth(root):
    if(root is None):
        return 0 
    if(root.left is None and root.right is None):
        return 1
     
    left_side = 1 + maxDepth(root.left)
    right_side = 1 + maxDepth(root.right)
    return max(left_side,right_side)



# print(maxDepth(root))

def bottomUpLevelOrderTraversalRecursive(node,level,result):
    if not node:
        return

    if len(result) <= level:
        print(node.val)
        result.insert(0,[])

    result[len(result)-level-1].append(node.val)

    bottomUpLevelOrderTraversalRecursive(node.left, level + 1, result)
    bottomUpLevelOrderTraversalRecursive(node.right, level + 1, result)
    

def bottomUpLevelOrderTraversal(root):
    result = []
    bottomUpLevelOrderTraversalRecursive(root,0,result)
    return result





def minDepth(root):
    if(root is None):
        return 0 
    
    if(root.left is None and root.right is None):
        return 1
    
    if(root.left is None and root.right is not None):
        return 1 + minDepth(root.lef)
     
    left_side = 1 + minDepth(root.left)
    right_side = 1 + minDepth(root.right)
    return min(left_side,right_side)





# print(minDepth(root))


