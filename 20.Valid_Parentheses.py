# https://leetcode.com/problems/valid-parentheses/

def isvalid(s):
        l = []
        for bracket in s:
            if bracket in ("(", "[", "{"):
                l.append(bracket)
            elif (l and bracket == ")" and l[-1] == "(") or (l and bracket == "]" and l[-1] == "[") or (l and bracket == "}" and l[-1] == "{"):
                l.pop()
            else:
                return False
        if l:
            return False
        else:
            return True


ex = "))"
print(isvalid(ex))
