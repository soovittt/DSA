# Write a function, treeSum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_sum(root):
  if(root is None):return 0 
  frontier_queue = []
  visited = []
  frontier_queue.append(root)
  visited.append(root.val)
  sum_val  = root.val
  while(frontier_queue):
    current = frontier_queue.pop()
    if(current.left is not None):
      frontier_queue.insert(0,current.left)
      visited.append(current.left.val)
      sum_val += current.left.val
    if(current.right is not None):
      frontier_queue.insert(0,current.right)
      visited.append(current.right.val)
      sum_val += current.right.val
  return sum_val



a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

tree_sum(a) # -> 21