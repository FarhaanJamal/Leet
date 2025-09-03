class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def perform_backspace(string, pointer):
            backspace = 0
            while pointer >= 0:
                print(pointer)
                if string[pointer] == "#":
                    backspace += 1
                elif backspace > 0:
                    backspace -=1
                else:
                    break
                pointer -=1
            return pointer

        s_p, t_p = len(s)-1, len(t)-1
        while s_p >= 0 or t_p >= 0:
            print(s_p, t_p)
            s_p = perform_backspace(s, s_p)
            t_p = perform_backspace(t, t_p)
            if s_p < 0 and t_p < 0:
                return True
            if s_p < 0 or t_p < 0:
                return False
            if s[s_p] != t[t_p]:
                return False
            s_p -= 1
            t_p -= 1
        
        return True

