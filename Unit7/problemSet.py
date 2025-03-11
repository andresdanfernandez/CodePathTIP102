"""
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

Implement the solution iteratively without the use of the len() function.

Implement the solution recursively.

Discuss: what are the similarities between the two solutions? What are the differences?
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
Example Output:

3
4
"""
"""
def count_suits_iterative(suits):
    count = 0
    for i in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if len(suits) == 1:
        return 1
    
    return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))"
"""


"""
Problem 2: Collecting Infinity Stones
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power using a recursive approach.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def sum_stones(stones):
    pass
Example Usage:

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
Example Output:

105
68
"""

"""
def sum_stones(stones):
    if not stones:
        return 0
    
    return stones[0] + sum_stones(stones[1:])


print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))"""

"""
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of unique suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
    
Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

Example Output:

3
2
"""

"""
def count_suits_iterative(suits):
    unique_suits = set()
    for suit in suits:
        unique_suits.add(suit)
    return len(unique_suits)

def count_suits_recursive(suits):
    def helper(index, unique_suits):
        if index == len(suits):  
            return len(unique_suits)
        
        unique_suits.add(suits[index])  
        return helper(index + 1, unique_suits)  
    
    return helper(0, set())  

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))"""

"""
Problem 4: Calculating Groot's Growth
Groot grows according to a pattern similar to the Fibonacci sequence. Given n, find the height of Groot after n months using a recursive method.

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def fibonacci_growth(n):
    pass
Example Usage:

print(fibonacci_growth(5))
print(fibonacci_growth(8))
Example Output:

5
21
"""

"""
def fibonacci_growth(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)
        
print(fibonacci_growth(5))
print(fibonacci_growth(8))     
"""

"""Problem 5: Calculating the Power of the Fantastic Four
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. Write a recursive function that calculates the power of 4 raised to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def power_of_four(n):
    pass
Example Usage:

print(power_of_four(2))
print(power_of_four(-2))
Example Output:

16
Example 1 Explanation: 2 to the 4th power (4 * 4) is 16. 
16
Example 2 Explanation: -2 to the 4th power is 1/(4 * 4) is 0.0625.
"""
"""
def power_of_four(n):
    if n == 0:
        return 1
    elif n > 0:
        return 4 * power_of_four(n - 1)
    else:
        return (1 / 4) * power_of_four(n + 1)

print(power_of_four(2))
print(power_of_four(-2))
"""

"""Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their strengths, find the maximum strength using a recursive approach without using the max() function.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def strongest_avenger(strengths):
    pass
Example Usage:

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
Example Output:

100
Example 1 Explanation: The maximum strength among the Avengers is 100.

90
Example 2 Explanation: The maximum strength among the Avengers is 90.
"""

"""
def strongest_avenger(strengths):

    if len(strengths) == 1:
        return strengths[0]
    else:
      
        return max(strengths[0], strongest_avenger(strengths[1:]))
        
print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))      
"""

"""Problem 7: Counting Vibranium Deposits
In Wakanda, vibranium is the most precious resource, and it is found in several deposits. Each deposit is represented by a character in a string (e.g., "V" for vibranium, "G" for gold, etc.)

Given a string resources, write a recursive function count_deposits() that returns the total number of distinct vibranium deposits in resources.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def count_deposits(resources):
    pass
Example Usage:

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))
Example Output:

5
2
Example 2 Explanation: There are two characters "V" in the string "VXVYGA", 
therefore there are two vibranium deposits in the string.
"""
"""
def count_deposits(resources):
    
    if not resources:
        return 0
    else:
        
        if resources[0] == 'V':
            return 1 + count_deposits(resources[1:])
        else:
            return count_deposits(resources[1:])
            
print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))            
"""


"""Problem 8: Merging Missions
The Avengers are planning multiple missions, and each mission has a priority level represented as a node in a linked list. You are given the heads of two sorted linked lists, mission1 and mission2, where each node represents a mission with its priority level.

Implement a recursive function merge_missions() which merges these two mission lists into one sorted list, ensuring that the combined list maintains the correct order of priorities. The merged list should be made by splicing together the nodes from the first two lists.

Return the head of the merged mission linked list.

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    pass
Example Usage:

mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

"""class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    
    if mission1 is None:
        return mission2
    if mission2 is None:
        return mission1

    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2
    
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))
"""