#!!!!UMPIRE

# You are given a sorted list of integers. Write a function that removes the duplicate numbers
# from the list in-place (i.e., without creating a new list) and returns the length of the list
# after duplicates have been removed. The relative order of the elements should be maintained, and
# the remaining elements must be in the original order.

# Example Input 1: nums = [1, 1, 2]
# Example Output 1:
# Length: 2
# Modified List: [1, 2]

# Example Input 2: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Example Output 2:
# Length: 5
# Modified List: [0, 1, 2, 3, 4]

# U - we take in sorted list of ints, we want to remove duplicate values (in place), keep relative order, return length
# P - make a seen set, iterate through list with (for i in range(len(nums))) add to seenSet if haven't seen, if we come across a value in seenSet then del nums[i],
# after for loop ends, return len(nums)

from collections import defaultdict

def remove_duplicates(nums):
    seenSet = set()

    hashMap = defaultdict(list)
    
    for i in range(len(nums)):

        if nums[i] in seenSet:
            hashMap[nums[i]].append(i)

        seenSet.add(nums[i])

    for key, value in hashMap.items():
            
        if key in seenSet:
            i = 0
            while i < len(value):
                del nums[key]
                i += 1
            
        
    return len(nums)

print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1, 1, 2]))
        
