class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_includes(root, target):
  
  if(root is None):
    return False
  frontier_queue = []
  visited = []
  frontier_queue.append(root)
  visited.append(root.val)
  while(frontier_queue):
    current = frontier_queue.pop()
    if(current.val==target):
       return True
    if(current.left is not None):
        if(current.left.val not in visited):
            frontier_queue.insert(0,current.left)
            visited.append(current.left.val)
    if(current.right is not None):
        if(current.right.val not in visited):
            frontier_queue.insert(0,current.right)
            visited.append(current.right.val)
  return False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(tree_includes(a, "g"))