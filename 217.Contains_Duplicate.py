# https://leetcode.com/problems/contains-duplicate/

def containsduplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False


if __name__=='__main__':
    # n = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(containsduplicate(n))
