class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        most_water = 0

        while left < right:
            curr_h = min(heights[left], heights[right])
            most_water = max(most_water, (right - left) * curr_h)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return most_water