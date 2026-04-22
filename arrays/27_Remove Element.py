class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        j = len(nums) - 1
        while j >= 0:
            if nums[j] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1
            j -= 1
        return i + 1

        ###double pointers solution