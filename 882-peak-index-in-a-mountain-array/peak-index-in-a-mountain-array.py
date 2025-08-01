class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for ind in range(1, len(arr)):
            if arr[ind-1] <= arr[ind]:
                continue
            return ind-1
        return 0