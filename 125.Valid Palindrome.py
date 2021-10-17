# https://leetcode.com/problems/valid-palindrome/

def ispalindrome(s):
    l = len(s)
    if l < 1: return True
    st, fin = 0, l - 1
    while fin - st > 0:
        if s[st].isalnum() and s[fin].isalnum():
            if s[st].lower() != s[fin].lower():
                return False
        elif not s[fin].isalnum():
            fin -= 1
            continue
        elif not s[st].isalnum():
            st += 1
            continue
        st += 1
        fin -= 1
    return True


if __name__ == '__main__':
    print(ispalindrome("aa"))