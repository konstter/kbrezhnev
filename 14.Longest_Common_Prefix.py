

# https://leetcode.com/problems/longest-common-prefix/

def longest_common_prefix(strs):
    if len(strs) == 1:
        return strs[0]
    else:
        strs.sort()
        prefix = ''
        for i, val in enumerate(strs[0]):
            if val == strs[-1][i]:
                prefix += val
            else:
                return prefix
        return prefix


strs1 = ["abab","aba","abc"]
print(longest_common_prefix(strs1))