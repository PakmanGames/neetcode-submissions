class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        res = 0
        while right < len(nums) - 1:
            far = 0
            for i in range(left, right + 1):
                far = max(far, i + nums[i])
            left = right + 1
            right = far
            res += 1
        return res