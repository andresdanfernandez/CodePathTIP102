from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Problem 1
"""class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right"""

"""
root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh", TreeNode("Fuji"), TreeNode("Opal"))
root.right = TreeNode("Granny Smith", TreeNode("Crab"), TreeNode("Gala"))
print_tree(root)
"""

# Problem 2
"""
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
"""
# Problem 3
"""
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

 # Problem 4 
def right_vine_rec(root, acc=None):
    
    if acc is None:
       acc = []
       
    if not root:
        return acc
    
    acc.append(root.val)

    if not root.right:

        return acc
        
    return right_vine_rec(root.right, acc)
    """

# Problem 5
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(countLeaves(oak1))
print(countLeaves(oak2))
"""

# Problem 6

"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def surveyTree(root):
    if root is None:
        return []
    return surveyTree(root.left) + surveyTree(root.right) + [root.val]

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
print(surveyTree(magnolia))
"""

# Problem 7
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvestBerries(root, threshold):
    if root is None:
        return 0
    left_sum = harvestBerries(root.left, threshold)
    right_sum = harvestBerries(root.right, threshold)
    return (root.val if root.val > threshold else 0) + left_sum + right_sum

bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvestBerries(bush, 6))
print(harvestBerries(bush, 30))
"""

# Problem 8
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def findFlower(root, flower):
    if root is None:
        return False
    if root.val == flower:
        return True
    return findFlower(root.left, flower) or findFlower(root.right, flower)

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(findFlower(flower_field, "Lilac"))
print(findFlower(flower_field, "Hibiscus"))
"""