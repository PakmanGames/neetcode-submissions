class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        lmax = height[left]
        rmax = height[right]

        while left < right:
            if lmax < rmax:
                left += 1
                lmax = max(lmax, height[left])
                res += lmax - height[left]
            else:
                right -= 1
                rmax = max(rmax, height[right])
                res += rmax - height[right]
        return res