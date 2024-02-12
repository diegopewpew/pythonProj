class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
      # Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               # If there is no left child, create a new node and set it as the left child
               self.left = Node(data)
            else:
               # If there is a left child, recursively insert the data into the left subtree
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  # If there is no right child, create a new node and set it as the right child
                  self.right = Node(data)
               else:
                  # If there is a right child, recursively insert the data into the right subtree
                  self.right.insert(data)
      else:
         # If the current node has no data, set the data to the input value
         self.data = data

   def PrintTree(self):
      # In-order traversal of the tree (left, root, right)
      if self.left:
         self.left.PrintTree()
      print(self.data, end=' ')
      if self.right:
         self.right.PrintTree()

   def depth(self):
      # Calculate the depth of the tree using recursion
      if not self.data:
         # Base case: If the node has no data, the depth is 0
         return 0
      else:
         # Recursive case: Calculate the depth of the left and right subtrees
         left_depth = self.left.depth() if self.left else 0
         right_depth = self.right.depth() if self.right else 0
         # Return the maximum depth of the left and right subtrees, plus 1 for the current node
         return max(left_depth, right_depth) + 1

root = None

while True:
   val = input("Enter a value (or 'q' to quit): ")
   if val == 'q':
      break
   if not root:
      # If the tree is empty, create a new root node
      root = Node(int(val))
   else:
      # Insert the value into the existing tree
      root.insert(int(val))

print("The tree is:")
root.PrintTree()
print("\nIts depth is:", root.depth())