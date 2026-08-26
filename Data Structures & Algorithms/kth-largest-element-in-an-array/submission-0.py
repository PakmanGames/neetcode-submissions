class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums) # O(nlogn) time, O(n) space into max heap
        # end lenght should be curr length - k + 1
        for _ in range(k - 1):
            heapq.heappop_max(nums)
        return heapq.heappop_max(nums)
