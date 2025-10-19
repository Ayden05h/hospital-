class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
    




class DoctorTree:
    def __init__(self):
        self.root = None
        
    def insert(self, name):
        new_node =DoctorNode(name)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_rec(self.root, new_node)
            
    def _insert_rec(self, current_node, new_node):
        if new_node.name < current_node.name:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_rec(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_rec(current_node.right, new_node)
                
    def inorder_traversal(self):
        return self._inorder_rec(self.root)
    
    def _inorder_rec(self, node):
        if node is None:
            return []
        return (self._inorder_rec(node.left) + [node.name] + self._inorder_rec(node.right))
    



# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.insert("Dr. Hall")
tree.insert("Dr. Johnson")
tree.insert("Dr. Williams")
tree.insert("Dr. Zimm")

print("doctors in appropriate order:")
print(tree.inorder_traversal())

'''
design memo_
#1 Why is a tree appropriate for the doctor structure?
-A tree structure is appropriate because it represents hierarchical relationships effectively, allowing for efficient searching, insertion, and traversal of doctor names in a sorted manner. Due to this doctors can be looked up quicker by name or any other attributes
-Every node represents a doctor, the left and right are a more sorted structure.
-Due to the speed of insertion, deleting, and arrival time, this makes a tree perfect for structured applications where order is important.
#2 When might a software engineer use preorder, inorder, or postorder traversals?
-An engineer would use a preorder traversal when they need to create a copy of the tree or need to get a prefix expression on an expression tree. Basically when they want to process a parent node before the children nodes. 
-An inorder traversal is used when they need to retrieve data in a sorted order, especially in binary search trees. This is useful for operations like printing the tree's contents in ascending order.
-Lastly a postorder traversal is useful when deleting nodes or freeing memory, as it processes child nodes before their parent nodes. It's also used in scenarios where the parent node's processing depends on the results of its children, such as evaluating expression trees.
#3 How do heaps help simulate real-time systems like emergency intake?
-Heaps are ideal for simulating real-time systems like emergency intake because they efficiently manage priority-based data. In an emergency room, patients need to be treated based on the severity of their conditions rather than their arrival times. A min-heap allows for quick access to the highest-priority patient (the one with the lowest priority value) in logarithmic time, ensuring that critical cases are addressed promptly.


'''