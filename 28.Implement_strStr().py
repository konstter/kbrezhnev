# https://leetcode.com/problems/implement-strstr/

def strstr(haystack, needle):
    if needle == "":
        return 0
    else:
        l_hay, l_n = len(haystack), len(needle)
        for i, item in enumerate(haystack):
            if item == needle[0] and l_n + i <= l_hay:
                print(haystack[i: i + l_n])
                if haystack[i: i + l_n] == needle:
                    return i
        return -1


h = "hello"
n = "ll"
print(strstr(h, n))
