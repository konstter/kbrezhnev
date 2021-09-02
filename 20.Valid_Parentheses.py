# https://leetcode.com/problems/valid-parentheses/

def isvalid(s):
        l = []
        d = {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket in ("(", "[", "{"):
                l.append(bracket)
            elif l and d[bracket] == l[-1]:
                l.pop()
            else:
                return False
        if l:
            return False
        else:
            return True


ex = "{"
print(isvalid(ex))
