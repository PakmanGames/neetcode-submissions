class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        operate on sorted nums # O(nlogn)
        nums[j] + nums[k] = - nums[i]
        two pointer approach pointing inwards from j and k
        where j = left and k = right

        '''
        res = []
        nums.sort() # O(nlogn) time complexity

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr = - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[left] + nums[right]
                if sums == curr:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right + 1]:
                        right -= 1
                elif sums < curr:
                    left += 1
                elif sums > curr:
                    right -= 1
        return res