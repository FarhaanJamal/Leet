class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def two_pointers(s):
            ln = len(s)
            if ln == 0:
                return []
            l, r = -1, 0
            lst = list(s)
            while l < r and r < len(lst):
                print(l, r, lst)
                if lst[r] == "#":
                    if l != -1:
                        lst.pop(l)
                        l-=1
                        r-=1
                    lst.pop(r)
                    if r > 0:
                        l-=1
                        r-=1                    
                    continue
                r+=1
                l+=1
            return lst
        print(two_pointers(s), two_pointers(t))
        return two_pointers(s) == two_pointers(t)