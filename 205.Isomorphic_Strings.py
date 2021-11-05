# https://leetcode.com/problems/isomorphic-strings/

def isisomorphic(s, t):
    isodict = {}
    while s:
        if s[0] in isodict:
            if isodict[s[0]] != t[0]:
                return False
        else:
            if t[0] in isodict.values():
                return False
            isodict[s[0]] = t[0]
        s, t = s[1:], t[1:]
    return True


if __name__ == '__main__':
    s_, t_ = 'badc', 'baba'
    print(isisomorphic(s_, t_))
