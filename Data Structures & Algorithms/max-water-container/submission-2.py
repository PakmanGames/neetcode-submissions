class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        [1,7,2,5,4,7,3,6]
         0 1 2 3 4 5 6 7
        output: 36

        curr_max = 0

        nested solution: O(n^2) time complexity

        area = length * width
        width = high_index - low_index
        length = min(heights[high_index], hights[low_index])

        goal is to find max amount of water

        [7,1,2,5,4,7,3,6]

        left = 0
        right = len(heights) - 1 # last index

        while left < right:
            curr_max = max(curr_max, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return curr_max
        '''
        curr_max = 0
        left = 0
        right = len(heights) - 1 # last index

        while left < right:
            curr_max = max(curr_max, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return curr_max
        '''
        len(heights) = 0
        '''