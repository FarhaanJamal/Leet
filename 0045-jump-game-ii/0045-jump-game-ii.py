class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        dct = {0:[0]}
        flg_m = [True, False]
        flg = [True, False]
        d_i = 0
        lst = []
        for i in range(len(nums)):
            if max(dct[d_i]) < i:
                d_i += 1
                lst = []
                flg_m.append(False)
                flg.append(False)
            mx = max(dct[d_i])
            if mx + nums[i] > mx:
                mx = i + nums[i]
                if flg_m[d_i+1]:
                    lst = dct[d_i+1]
                    lst.append(mx)
                    dct[d_i+1] = lst
                else:
                    dct[d_i+1] = [mx]
                    flg_m[d_i+1] = True
                    flg[d_i+1] = True
            if flg[d_i+1]:
                if max(dct[d_i+1]) >= len(nums)-1:
                    return d_i+1