class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ss = set()
        left = 0
        for i in range(len(nums)):
            if i > k:
                ss.remove(nums[i - k - 1])
            if nums[i] in ss:
                return True
            ss.add(nums[i])
        return False