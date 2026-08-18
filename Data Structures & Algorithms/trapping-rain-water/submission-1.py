class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        l_b = height[left]
        r_b = height[right]
        res = 0

        while left < right:
            h = 0
            if l_b < r_b:
                left += 1
                l_b = max(l_b, height[left])
                h = height[left]
            else:
                right -= 1
                r_b = max(r_b, height[right])
                h = height[right]
            res += max(0, min(l_b, r_b) - h)
        return res