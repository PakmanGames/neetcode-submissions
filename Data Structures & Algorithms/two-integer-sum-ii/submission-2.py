class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if left < right and numbers[left] + numbers[right] < target:
                left += 1
            elif left < right and numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return [-1, -1]