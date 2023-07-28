class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            #nums1 = nums2.copy()
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0:
            pass
        else:
            i = 0
            j = 0
            inst = 0
            while i < m+n:
                try:
                    if not all([val == 0 for val in nums1[i:]]):
                        if (nums1[i] <= nums2[j]):
                            i += 1
                            continue
                        else:
                            nums1.insert(i, nums2[j])
                            nums1.pop()
                            inst += 1
                            i += 1
                            j += 1
                            #print(nums1, inst, i, j)   
                    else:
                        nums1[i] = nums2[j]
                        i += 1
                        j += 1
                except IndexError:
                            break