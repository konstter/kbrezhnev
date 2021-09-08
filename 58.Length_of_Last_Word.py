# https://leetcode.com/problems/length-of-last-word/

def lengthoflastword(s):
        k, p = 0, 0
        for char in s[::-1]:
            p -= 1
            if char != ' ':
                k += 1
                if abs(p) != len(s):
                    if s[p - 1] == ' ':
                        return k
        return k


str = "   "
print(lengthoflastword(str))
