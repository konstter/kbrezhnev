# https://leetcode.com/problems/valid-palindrome/

def ispalindrome(s):
    l = len(s)
    if l < 1: return False
    st, fin = 0, l - 1
    while fin - st > 0:
        if s[st].isalnum() and s[fin].isalnum():
            if s[st].lower() != s[fin].lower():
                return False
            else:
                st += 1
                fin -= 1
        elif not s[fin].isalnum():
            fin -= 1
        elif not s[st].isalnum():
            st += 1
        else:
            st += 1
            fin -= 1
    return True


if __name__ == '__main__':
    print(ispalindrome("ab"))