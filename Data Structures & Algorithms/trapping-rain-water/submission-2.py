class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        l_max = height[left]
        r_max = height[right]
        res = 0

        while left < right:
            cur_height = min(l_max, r_max)
            if height[left] < height[right]:
                left += 1
                l_max = max(l_max, height[left])
                res += max(cur_height - height[left], 0)
            else:
                right -= 1
                r_max = max(r_max, height[right])
                res += max(cur_height - height[right], 0)
        return res
        # O(n) time visits each element at most once
        # O(1) space