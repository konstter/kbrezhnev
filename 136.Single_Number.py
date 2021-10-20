# https://leetcode.com/problems/single-number/

def singlenumber(nums):
    res = nums[0]
    for x in range(1, len(nums)):
        res ^= nums[x]
    return res


if __name__ == '__main__':
    print(singlenumber([5, 2, 3, 2, 5]))
# XOR operation
    print(5^2)
    print(7^3)
    print(4^2)
    print(6^5)