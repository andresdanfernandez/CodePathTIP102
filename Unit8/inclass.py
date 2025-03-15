"""
Problem 2: Calculating Yield
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
The root has a string value of either "+", "-", "*", or "/".
The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  pass
Example Usage:

     +        | 0
   /   \      | 
  7     5     | 1
          \   | 
            6 | 2
 
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))
Example Output:

12

"""

# Understand: We are given a binary tree that has a root and 2 children, the root is an arithmetic operation and the children are integer values. We want to return the left child {insert operation} right child.

# Plan: 
#     - Base Case: When the node is of value type int return the value
#     - Two variables = left_child, right_child
#     - Use conditionals to return when node isn't of type int and return operation 

# Implement:

"""
Match pattern:

match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# Big O
# Time: O(n)
# Space: 

def calculate_yield(root):
  if isinstance(root.val, int):
     return root.val
  
  left_child = calculate_yield(root.left) # 7
  right_child = calculate_yield(root.right) # 5

  match root.val:
    case "+":
        return left_child + right_child
    case "-":
        return left_child - right_child
    case "*":
        return left_child * right_child
    case "/":
        return left_child / right_child if right_child != 0 else "Can't divide by zero!"
    case _:
        return "Not a valid operation!"
  

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree)) # 7 + 5 = 12
apple_tree = TreeNode("-", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree)) # 7 - 5 = 2
apple_tree = TreeNode("*", TreeNode(2), TreeNode(5))
print(calculate_yield(apple_tree)) # 2 * 5 = 10
apple_tree = TreeNode("/", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree)) # 7 / 5 = 1.4
apple_tree = TreeNode(".", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree)) # 7 . 5 = "Not a valid operation!"
apple_tree = TreeNode("/", TreeNode(7), TreeNode(0))
print(calculate_yield(apple_tree)) # 7 / 0 = "Can't divide by zero!"


'''
Problem 3: Ivy Cutting
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  pass
Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
Example Output:

['Root', 'Node2', 'Leaf3']
['Root']
'''

# Understand: We are given a binary tree containing nodes. We want to iterate through the tree until we find the rightmost node with no children. If root has no right child return root. Store each value as we work down the right path. 

# Plan: Create a path list to store our nodes 
# Create a current node which is = root
# Traverse through the binary tree using a while loop (while curr)
# Inside the while loop append the current node to our path list
# Traverse to next right node
# Return our path list


# rightvine(root)
# returns 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):

  if not root:
    return []
  
  if not root.right:
    return [root]

  path = []
  current = root

  while current:
     path.append(current.val)
     current = current.right

  return path

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

def right_vine_rec(root, acc=None):
    
    if acc is None:
       acc = []
       
    if not root:
        return acc
    
    acc.append(root.val)

    if not root.right:

        return acc
        
    return right_vine_rec(root.right, acc)


ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

#['Root', 'Node2', 'Leaf3']

# did the addition outside of the recurisve call and returned acc if node doesnt exist since we dont add anything

print(right_vine_rec(ivy1))
print(right_vine(ivy1))