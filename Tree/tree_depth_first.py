# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.
# Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


#Algorithm 

def depth_first_values(root):
    if(root is None):return []
    visited = []
    sequence_stack = []
    sequence_stack.append(root)
    while(sequence_stack):
       current =  sequence_stack.pop()
       visited.append(current.val)
       if(current.right is not None):sequence_stack.append(current.right)
       if(current.left is not None):sequence_stack.append(current.left)
    return visited

        

    

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f



# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# a.right = b;
# b.left = c;
# c.right = d;
# d.right = e;
depth_first_values(None)