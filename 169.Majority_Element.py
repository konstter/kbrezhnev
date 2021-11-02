#https://leetcode.com/problems/majority-element/

def majorityelement(nums):
    nums.sort()
    lnum = len(nums)
    return nums[lnum // 2]

if __name__ == '__main__':
    # n = [2, 2, 1, 1, 1, 2, 2]
    n = [1, 3, 1, 3, 3, 3]
    print(majorityelement(n))

