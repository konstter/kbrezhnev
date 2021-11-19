# https://leetcode.com/problems/valid-anagram/

def isanagram(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    for letter in t:
        if letter not in s_list:
            return False
        else:
            s_list.remove(letter)
    return True


if __name__=='__main__':
    s1 = 'anagram'
    t1 = 'nagaram'
    print(isanagram(s1, t1))

