"""
Problem:
Given a sorted array numbers, find two numbers that sum up to a specific target. Return their indices (1-indexed).
"""

# Input: 
numbers = [2,7,11,15]
target = 9
Output= [1,2]

# take 2 pointers - index starts with 0.
left = 0
right = len(numbers) - 1

while left < right:
    if numbers[left] + numbers[right] > target:
        pass