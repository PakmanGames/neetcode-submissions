class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_t = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == new_t:
                    return [i, j]
        