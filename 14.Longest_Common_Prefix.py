

# https://leetcode.com/problems/longest-common-prefix/

def longest_common_prefix(strs):
    s = strs[0]
    del strs[0]
    if not strs:
        return s
    else:
        prefix = ""
        sl = len(s)
        for elem in strs:
            tmp = ""
            pl = len(prefix)
            i = len(elem)
            for j in range(i):
                if j < sl:
                    if s[j] == elem[j]:
                        tmp += elem[j]
                    else:
                        break
            if not tmp:
                return tmp
            elif not prefix or pl > len(tmp):
                prefix = tmp
        return prefix


strs1 = ["a", "a", "b"]
print(longest_common_prefix(strs1))




