class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        mid_m = (left + right) // 2

        # O(log(m))
        while left <= right:
            mid_m = (left + right) // 2
            if target < matrix[mid_m][0]:
                right = mid_m - 1
            elif target > matrix[mid_m][len(matrix[mid_m]) - 1]:
                left = mid_m + 1
            else:
                break
        left = 0
        right = len(matrix[0]) - 1
        if target > matrix[mid_m][right] or target < matrix[mid_m][left]:
            return False
        # O(log(n))
        while left <= right:
            mid_n = (left + right) // 2
            if target > matrix[mid_m][mid_n]:
                left = mid_n + 1
            elif target < matrix[mid_m][mid_n]:
                right = mid_n - 1
            elif target == matrix[mid_m][mid_n]:
                return True
        return False
        # Space: O(1)
        # Time: O(log(m) + log(n)) = O(log(m*n))