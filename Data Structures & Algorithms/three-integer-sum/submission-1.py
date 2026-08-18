class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums[j] + nums[k] = - nums[i]

        check for duplicate i and check for duplicate j and k if match -nums[i]

        '''
        nums.sort() # O(nlogn) time
        res = []
        for i in range(len(nums)): # O(n)
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            curr = - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right: # O(n)
                currSum = nums[left] + nums[right]
                if currSum == curr:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left - 1] == nums[left]:
                        left += 1
                    right -= 1
                    while right > 0 and nums[right + 1] == nums[right]:
                        right -= 1
                elif currSum < curr:
                    left += 1
                elif currSum > curr:
                    right -= 1
        return res
        # total time complexity is O(n^2)

