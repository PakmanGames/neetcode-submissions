class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        def houseRobber(houses):
            dp = [0] * (len(houses) + 1)
            for i in range(len(houses)):
                if i == 0:
                    dp[i] = houses[i]
                elif i == 1:
                    dp[i] = max(dp[i - 1], houses[i])
                else:
                    dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[len(houses) - 1]
        
        return max(houseRobber(nums[:len(nums) - 1]), houseRobber(nums[1:]))