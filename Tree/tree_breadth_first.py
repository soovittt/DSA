# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root):
  if(root is None):return []
  frontier_queue = []
  visited = []
  frontier_queue.append(root)
  visited.append(root.val)
  #print("before while loop fq : ",[f.val for f in frontier_queue])
  #print("before while loop visited : ",visited)
  while(frontier_queue):
    current = frontier_queue.pop()
    # visited.append(current.val)
    #print("current : ",current.val)
    
    if(current.left is not None):
        if(current.left.val not in visited):
            frontier_queue.insert(0,current.left)
            visited.append(current.left.val)
    if(current.right is not None):
        if(current.right.val not in visited):
            frontier_queue.insert(0,current.right)
            visited.append(current.right.val)
    #print("in while loop fq : ",[f.val for f in frontier_queue])
    #print("in while loop visited : ",visited)



def breadth_first_values_recursively(root):
   if(root==None):
      return []
   lval = breadth_first_values_recursively(root.left)
   rval = breadth_first_values_recursively(root.right)
   return lval + rval + [root.val]

    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h


print(breadth_first_values(a))