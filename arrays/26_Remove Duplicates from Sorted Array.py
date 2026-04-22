class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 1 ### start from the second element, since the first element is already unique
        j = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[j - 1]:
                i += 1
            if i < len(nums):
                nums[j] = nums[i]
                i += 1
                j += 1
        return j
        ###double pointers solution