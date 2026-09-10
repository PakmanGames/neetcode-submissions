class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # O(n) space
        for num in nums: # O(n) time
            freq[num] = freq.get(num, 0) + 1
        # return sorted(freq, key=lambda frequency: freq.keys())[:k]

        '''
        O(nlogk)
        [1,2,2,3,3,3]

                1, 1
            2, 1

            heap item [item, count, status]
            if 2 alr in heap, find and pop 2,
            heappush new item [item, count + 1, status]
                2, 2
            1, 1

                2, 2
            1, 1    3, 1

                2, 2
            3, 2    1, 1
        
                3, 3
            2, 2    1, 1

            do k times:
            heapq.heappop_max()

        freq {
        3: 3
        2: 2
        1: 1
        }

        counts should be in the heap

                3
            2       1

        counts should map to items???
        '''
        heap = []
        for val in freq.values():
            heapq.heappush_max(heap, val) # O(logn)
        
        res = []
        k_frequencies = heapq.nlargest(k, heap)

        for ke, val in freq.items():
            if val in k_frequencies:
                res.append(ke)
            if len(res) == k:
                return res
        return res
        # time: ???
        # space: O(n)


            















