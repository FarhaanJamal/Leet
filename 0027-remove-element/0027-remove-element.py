class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
        i=0
        while i<=k:
            try:
                if nums[i] == val:
                    nums.remove(val)
                    nums.append("_")
                else:
                    i += 1
            except IndexError:
                break 
        return k