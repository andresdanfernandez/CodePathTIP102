"""Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, 
such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, 
and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.

def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False

"""

"""
Understand:
    Clarify - each opening char should have correct closing char ex. (). 
              limited to ()[]{} assume no other char input.
              for result stack we want to make sure its empty becuase if it isn't the input isn't balanced.

Plan:
    - check length of input incase we return early.
    - we want to use a dict to store characters were looking for. {')':'('}
    - create a stack
    - iterate through input and store only opening brackets in the stack ['('] -> if we see a closing bracket (use dict) of same type ')' we can pop off stack
    - once we finish return if len(stack): return False else return True
    - return True if len(stack) == 0 else False

Implement:


"""

def is_valid_post_format(posts):

    if len(posts) <= 1:
        return False
    
    close_to_open = {
      ')': '(',
      ']': '[',
      '}': '{'
    }

    stack = []

    for char in posts:
        # current char is '(' | current ')'
        # []                  | ['(']
        # if closeToOpen[char] == stack[-1] => ) : ( 
        if char in close_to_open and stack:
            
            if close_to_open[char] == stack[-1]:
                stack.pop()
            
        else:
            stack.append(char)

    return True if len(stack) == 0 else False
    

print(is_valid_post_format("{([)]}"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))


"""
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to 
reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
  
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']

Understand:

    Clarify - can input include empty strings? "", " "


Plan:
    - if len(comments) == 0: return comments
    - stack = []
    - result = []
    - iterate through the comments and append to our stack
    - ["Great post!", "Love it!", "Thanks for sharing."] len 3
    - while stack:
        result.append(stack.pop())

    - return result


Implement: 

"""

def reverse_comments_queue(comments):
  if len(comments) == 0: return comments
  stack = []
  result = []
  for value in comments:
      stack.append(value)
      
  while stack:
      result.append(stack.pop())

  return result

  
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


"""
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical,
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string,
use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
Example Output:

True
False
💡Hint: Two Pointer Technique

Understand:
    Clarify:
      - empty title return false
      - we want to ignore cases, spaces, and punctuation
      - does even or odd lengths matter? xccx vs xcx xxeexx still be true?


Plan:
  - intiatialize left and right pointer 
  - use while to break out when left >= right
  - check title[left] == title[right] if chars are equal left++ right-- else or return false ?

==

"""

#Implement:

def is_symmetrical_title(title):

    # clean_txt = ''.join(ch for ch in title if ch not in string.punctuation)
    # print(clean_txt)

    clean_text = title.lower().strip("!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~").replace(" ", "")
    
    left = 0
    right = len(clean_text) - 1

    while left <= right:
        if clean_text[left] != clean_text[right]:
            return False
        
        left +=1 
        right -= 1
        
    return True

#asantaatnasa
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))


"""
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.


Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]
"""

def engagement_boost(engagements):
    squared_engagements = []
    
    # iterate through engagements using index
    for i in range(len(engagements)):
        # new variable = e[i] * e[i]
        squared_engagement = engagements[i] * engagements[i]
        # var gets appended to new list
        squared_engagements.append((squared_engagement, i))
    
    # new list is ordered in reverse?
    squared_engagements.sort(reverse=True)

    # create a new list with fixed length
    result = [0] * len(engagements)
    # start from the last index
    position = len(engagements) - 1
    
    # iterate through each sorted val and use position's index to reorder list
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result
# need to find smallest val ?
#                                     R
#                        L 
#                      [16, 1, 0, 9, 100]

print(engagement_boost([-4, -1, 0, 3, 10])) # [0, 1, 9, 16, 100]
print(engagement_boost([-7, -3, 2, 3, 11])) # [4, 9, 9, 49, 121]
