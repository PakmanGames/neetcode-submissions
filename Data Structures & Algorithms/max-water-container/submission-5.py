class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while left <= right:
            height = min(heights[left], heights[right])
            maxArea = max((right - left) * height, maxArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        '''
        height=[1,7,2,5,4,7,3,6]
                0,1,2,3,4,5,6,7
        '''