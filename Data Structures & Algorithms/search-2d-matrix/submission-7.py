class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (right + left) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                left = mid + 1
            else:
                left = mid
                break
        mid = left
        if not (0 <= mid < len(matrix)):
            return False
        left = 0
        right = len(matrix[mid]) - 1
        
        while left <= right:
            midd = (right + left) // 2
            if target < matrix[mid][midd]:
                right = midd - 1
            elif target > matrix[mid][midd]:
                left = midd + 1
            else:
                return True
        return False
        