"""
Problem: Two Sum
Date: 2026-04-21
Difficulty: Easy
Pattern: Hash Map

Idea:
Use a hash map to store seen values and check complement.

Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i