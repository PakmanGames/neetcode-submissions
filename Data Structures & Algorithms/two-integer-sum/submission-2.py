class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in numbers and i != numbers[target - nums[i]]:
                return [i, numbers[target - nums[i]]]