# https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def haspathsum(root, targetsum):
    if not root: return False
    s = []
    pathsum, tmp = 0, 0
    while True:
        if not root and s:
            item = s.pop()
            root = item[0].right
            tmp, pathsum = item[1], 0
        else:
            pathsum += root.val + tmp
            tmp = 0
            if not root.left and not root.right and pathsum == targetsum:
                return True
            s.append([root, pathsum])
            root = root.left
        if not root and not s:
            return False



# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)
# root.right.right.right.right = TreeNode(5)
# print(f'Result: {haspathsum(root, 15)}')


# root = TreeNode(-9)
# root.left = TreeNode(-3)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(-6)
# root.left.right.right = TreeNode(0)
# root.right = TreeNode(2)
# root.right.left = TreeNode(4)
# root.right.left.left = TreeNode(-5)
# root.right.right = TreeNode(0)
# print(f'Result: {haspathsum(root, -8)}')

root = TreeNode(1)
root.left = TreeNode(-2)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(-1)
root.left.right = TreeNode(3)
root.right = TreeNode(-3)
root.right.left = TreeNode(-2)
print(f'Result: {haspathsum(root, -4)}')