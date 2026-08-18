class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        def helper(numbers):
            dp = [0] * (len(numbers) + 1)
            for i in range(len(numbers)):
                if i == 0:
                    dp[i] = numbers[i]
                elif i == 1:
                    dp[i] = max(numbers[i], dp[i - 1])
                else:
                    dp[i] = max(dp[i - 1], dp[i - 2] + numbers[i])
            return dp[len(numbers) - 1]
        return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))