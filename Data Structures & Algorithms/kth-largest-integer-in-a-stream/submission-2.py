class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [n for n in nums]
        self.k = k
        # create a min heap here
        heapq.heapify(self.nums) # O(n) space, O(nlogn) time
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        # now there's only k items left

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # rebalance so there's only k items
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0] # the top item in the min heap is the kth largest


        
