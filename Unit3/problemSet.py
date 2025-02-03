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
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

"""
Problem 5: Content Cleaner
You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, you want to remove any pairs of 
adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. 
Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

def clean_post(post):
  pass
Example Usage:

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
Example Output:

post

s
"""

def clean_post(post):
    stack = []
    for char in post:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

"""
Problem 6: Post Editor
You want to add a creative twist to your posts by reversing the order of characters in each word within your post while still preserving whitespace and the initial word order. Given a string post, use a queue to reverse the order of characters in each word within the sentence.

def edit_post(post):
  pass
Example Usage:

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
Example Output:

tsooB ruoy tnemegegna htiw esehT spit
kcehC tuo ym tseval golv
"""
from collections import deque

def edit_post(post):
    q = deque()
    result = []
    
    for char in post:
        if char != ' ':
            q.append(char)
        else:
            reversed_word = ''
            while q:
                reversed_word = q.popleft() + reversed_word
            result.append(reversed_word)
            result.append(' ')

    reversed_word = ''
    while q:
        reversed_word = q.popleft() + reversed_word
    result.append(reversed_word)
    
    return ''.join(result)


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))


"""
Problem 7: Post Compare
You often draft your posts and edit them before publishing. Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will remain empty.

def post_compare(draft1, draft2):
  pass
Example Usage:

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
Example Output:

True
True
False
"""

def post_compare(draft1, draft2):
    def process_draft(s):
        stack = []
        for char in s:
            if char != '#':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return ''.join(stack)
    
    return process_draft(draft1) == process_draft(draft2)

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 