# https://leetcode.com/problems/valid-anagram/

def isanagram(s, t):
    if len(s) != len(t):
        return False
    s, t = sorted(s), sorted(t)
    if s == t:
        return True
    else:
        return False


if __name__=='__main__':
    s1 = 'anagram'
    t1 = 'nagaram'
    print(isanagram(s1, t1))

