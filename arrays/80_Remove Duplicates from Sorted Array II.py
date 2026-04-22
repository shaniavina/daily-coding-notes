class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 1
        j = 1
        count = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[j - 1]:
                i += 1
                count += 1
            if i < len(nums):
                if count > 1:
                    nums[j] = nums[j - 1]
                    j += 1
                    nums[j] = nums[i]
                    i += 1
                    j += 1
                
                else:
                    nums[j] = nums[i]
                    j += 1
                    i += 1
                count = 1
        if count > 1:
            nums[j] = nums[j - 1]
            j += 1
        return j

        ###double pointers solution