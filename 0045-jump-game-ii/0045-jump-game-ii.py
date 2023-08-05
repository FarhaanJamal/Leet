class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        dct = {0:[0]}
        d_i = 0
        lst = []
        for i in range(len(nums)):
            if max(dct[d_i]) < i:
                d_i += 1
                lst = []
            mx = max(dct[d_i])
            if mx + nums[i] > mx:
                mx = i + nums[i]
                try:
                    lst = dct[d_i+1]
                    lst.append(mx)
                    dct[d_i+1] = lst
                except KeyError:
                    dct[d_i+1] = [mx]
            try:
                if max(dct[d_i+1]) >= len(nums)-1:
                    return d_i+1
            except:
                pass