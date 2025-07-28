class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2 = [val * k for val in nums2]
        ans = 0
        for i in nums1:
            for j in nums2:
                if i % j == 0:
                    ans += 1
        return ans