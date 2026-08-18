class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = {}
        for i in range(len(nums)):
            if nums[i] not in keys:
                keys[nums[i]] = 1
            elif nums[i] in keys:
                keys[nums[i]] += 1
        
        res = []
        while len(res) < k:
            big_key = None
            big = 0
            for key, val in keys.items():
                if val > big:
                    big = val
                    big_key = key
            res.append(big_key)
            keys.pop(big_key)
        return res
