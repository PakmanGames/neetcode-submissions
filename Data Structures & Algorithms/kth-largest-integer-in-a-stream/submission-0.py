class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums) # O(nlogn)
        
        while len(self.nums) > self.k: # O(n)
            heapq.heappop(self.nums) # O(nlogn) for reheapify operations

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val) # O(nlogn) for maintaining heap property

        if len(self.nums) > self.k:
            heapq.heappop(self.nums) # O(nlogn) for reheapify operation
        return self.nums[0]