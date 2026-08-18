# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(arr, s, m, e):
            left = arr[s : m + 1]
            right = arr[m + 1 : e + 1]
            i = 0
            j = 0
            k = s

            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        def mergeSplit(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            m = (e + s) // 2
            mergeSplit(arr, s, m)
            mergeSplit(arr, m + 1, e)
            merge(arr, s, m , e)
            return arr
        return mergeSplit(pairs, 0, len(pairs) - 1)