# https://leetcode.com/problems/roman-to-integer/

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    l = len(s)
    if l == 1:
        return roman_dict[s]
    else:
        res = 0
        i = 0
        while i < l:
            if i + 1 < l:
                if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                    res += roman_dict[s[i + 1]] - roman_dict[s[i]]
                    i += 2
                else:
                    res += roman_dict[s[i]]
                    i += 1
            else:
                return res + roman_dict[s[i]]
        return res


st = 'MCMXCIV'
print(roman_to_int(st))
