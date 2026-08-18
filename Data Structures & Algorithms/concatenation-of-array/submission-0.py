class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * 2 * len(nums)
        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[i + len(nums)] = nums[i]
        return arr