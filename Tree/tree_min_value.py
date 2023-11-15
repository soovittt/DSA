class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value(root):
  min_val = root.val
  if(root is None):
    return False
  frontier_queue = []
  visited = []
  frontier_queue.append(root)
  visited.append(root.val)
  while(frontier_queue):
    current = frontier_queue.pop()
    if(current.val < min_val):
       min_val = current.val
    if(current.left is not None):
        if(current.left.val not in visited):
            frontier_queue.insert(0,current.left)
            visited.append(current.left.val)
    if(current.right is not None):
        if(current.right.val not in visited):
            frontier_queue.insert(0,current.right)
            visited.append(current.right.val)
  return min_val
  
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(tree_min_value(a)) 