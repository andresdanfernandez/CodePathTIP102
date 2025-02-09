"""
Problem 1: Arrange Guest Arrival Order
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. 
The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' 
meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should 
have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions.

def arrange_guest_arrival_order(arrival_pattern):
  pass
Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  -> 8
print(arrange_guest_arrival_order("DDD"))
print(arrange_guest_arrival_order("III"))
Example Output:

123549876 -> 9
4321
"""
# guest_order = ""
# len = 8

# for i in range(len + 1)

# where do we get the 9
#         reached last iteration bc + 1? -> add to stack [4,6,7,8,9] pop everything to result -> [1,2,3,5] -> [1,2,3,5,9,8,7,6]
#          D -> 8 -> add to stack [4,6,7,8] -> dont pop 
#          D -> 7 -> add to stack [4,6,7] -> dont pop 
#          D -> 6 -> add to stack [4,6] -> dont pop 
#          I -> 5 -> add to stack [4,5] -> pop stack -> [1,2,3,5]
#          D -> 4 -> add to stack [4] -> dont pop 
#          I -> 3 -> add to stack [3] -> pop stack -> ['1','2','3']
#          I -> 2 -> add to stack [2] -> pop stack -> ['1', '2']
# Stack:   I -> 1 -> add to stack [1] if char is 'I' pop stack to result - > ['1']
###


# Understand: 
# Guest can be either 'I' or 'D' and status can be '1' - '9'
#                                               
# 'I' -> next guest should have higher status
# 'D' -> next guest should have a lower status

# Plan:
# Create a stack, extract length from string, keep track of curr digit
# If our char is 'I' append to stack and increment digit
# 


# Implement:

def arrange_guest_arrival_order(arrival_pattern):
  stack = []
  n = len(arrival_pattern)
  status = 1
  result = []

  for i in range(n + 1):
    stack.append(str(status)) # -> [1,2,3,etc]
    status += 1

    if i == n or arrival_pattern[i] == 'I':
      while stack:
        result.append(stack.pop())

  return "".join(result)



print(arrange_guest_arrival_order("IIIDIDDD"))
print(arrange_guest_arrival_order("DDD"))

"""
Problem 2: Reveal Attendee List in Order
You are organizing an event where attendees have unique registration numbers. These numbers are provided in the list attendees.
 You need to arrange the attendees in a way that, when their registration numbers are revealed one by one, the numbers appear in increasing order.

The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:

Take the first registration number from the queue, pop it, and remove it from the queue.
If there are still registration numbers in the queue, take the next registration number and move it to the end of the queue.
If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
Return an ordering of the registration numbers that would reveal the attendees in increasing order.

def reveal_attendee_list_in_order(attendees):
  pass
  
Example Usage:

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))
print(reveal_attendee_list_in_order([1,1000]))  
Example Output:

attentee_list = [2,3,5,7,11,13,17]

removed = [17,11,3,7,2,13,5]

Original List: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]

[1,1000]
"""
