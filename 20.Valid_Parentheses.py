# https://leetcode.com/problems/valid-parentheses/

def isvalid(s):
    l = ["()", "{}", "[]"]
    while s != "":
        tmp = s
        for elem in l:
            i = tmp.find(elem)
            if i > -1:
                s = str.replace(tmp, elem, '')
        if s == tmp:
            return False
    return True

ex = "(){}{}"
print(isvalid(ex))