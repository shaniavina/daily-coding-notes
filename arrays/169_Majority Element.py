class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
            if counter[i] > len(nums) / 2:
                return i
        return None

        ###counter solution