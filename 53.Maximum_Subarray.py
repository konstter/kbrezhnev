# https://leetcode.com/problems/maximum-subarray/

def maxsubarray(nums):
    s = 0
    max = nums[0]
    for i in range(len(nums)):
        s += nums[i]
        if s > max:
            max = s
        if s <= 0:
            s = 0
    return max


n = [-5, -1, -3, -4]
print(maxsubarray(n))
