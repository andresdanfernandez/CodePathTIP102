"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


# Understand - search through list using Binary Search since its sorted, return true if found else false

# Plan - Use binary search

# Implememnt

def search(nums, target):

    left,right = 0, len(nums)-1

    m = (right + left) // 2

    while left < right:
        m = (right + left) // 2

        if nums[m] == target:
            return True
        elif nums[m] < target:
            left = (left + m) + 1
        elif nums[m] > target:
            right = (right - m) - 1
    
  
    return False
    

nums = [-1,0,3,5,9,12], 
target = 9
print(search(nums, target))
