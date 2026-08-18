class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for num in nums:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1

        frequent = []
        for _ in range(k):
            maximum = 0
            index = 0
            for element in elements:
                maximum = max(maximum, elements[element])
            for key in elements:
                if elements[key] == maximum:
                    index = key
            del elements[index]
            frequent.append(index)
        return frequent