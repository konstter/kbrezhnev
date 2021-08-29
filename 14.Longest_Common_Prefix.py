

# https://leetcode.com/problems/longest-common-prefix/

def longest_common_prefix(strs):
    if len(strs) == 1:
        return strs[0]
    else:
        strs.sort(key=len)
        s = strs[0]
        del strs[0]
        prefix = ''
        for i in range(len(s)):
            for elem in strs:
                if s[i] != elem[i]:
                    return prefix
            prefix += s[i]
        return prefix


strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))