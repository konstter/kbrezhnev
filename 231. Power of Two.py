# https://leetcode.com/problems/power-of-two/

def ispoweroftwo(n):
    if n <= 0 or '1' in bin(n)[3:]: return False
    return True

if __name__=='__main__':
    # print(ispoweroftwo(55))
    print(ispoweroftwo(1024))