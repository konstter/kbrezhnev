# https://leetcode.com/problems/convert-sorted-array-to-binary-search

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedarraytobst(nums):
    if not nums: return None
    c = len(nums) // 2
    root = TreeNode(nums[c])
    root.left = sortedarraytobst(nums[:c])
    root.right = sortedarraytobst(nums[c+1:])
    return root

nums = [3, 5, 8]
print(sortedarraytobst(nums).val)