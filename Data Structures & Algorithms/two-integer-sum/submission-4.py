class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if target - nums[i] in sums:
                return [sums[target - nums[i]], i]
            sums[nums[i]] = i
        return [-1, -1]