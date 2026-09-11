class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        7 and 6
        height = 6
        ans is 36
        1     7
        7 - 1 = length = 6
        height is min of both elements
        '''

        left = 0
        right = len(heights) - 1
        res = 0

        while left < right:
            height_left = heights[left]
            height_right = heights[right]
            height = min(height_left, height_right)
            res = max(res, height * (right - left))

            if height_left < height_right:
                left += 1
            else:
                right -= 1
        return res

        # Time O(n)
        # Space O(1)