class Node:
    """
    A class used to represent a Node in a doubly linked list.

    Attributes
    ----------
    data : any
        The data stored in the node.
    next : Node or None
        The reference to the next node in the list.
    prev : Node or None
        The reference to the previous node in the list.

    Methods
    -------
    __init__(self, data):
        Initializes the node with the given data and sets next and prev to None.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : any
            The data to be stored in the node.
        """
        self.data = data 
        self.next = None
        self.prev = None
        
        
def main():
    """
    The main function to demonstrate the creation and traversal of a doubly linked list.

    It creates four nodes and links them together in a doubly linked list.
    Then, it traverses the list forward from the first node and backward from the last node,
    printing the data of each node.
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    
    print("\nTraversing forward:")
    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")
    
    print("\nTraversing backward:")
    currentNode = node4
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.prev
    print("null")
    
    
    
    
    
main()