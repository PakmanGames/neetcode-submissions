class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        # O(log(m)) time
        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        row = (left + right) // 2
        left = 0
        right = len(matrix[row]) - 1

        # O(log(n)) time
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

        # Space: O(1)
        # Time: O(log(m) + log(n)) = O(log(m*n)) (log laws)