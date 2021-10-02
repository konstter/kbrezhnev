# https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def haspathsum(self, targetsum):
        if not root: return False
        self.f = False
        def foo(r, pathsum):
            if not r: return
            pathsum += r.val
            if not r.left and not r.right and pathsum == targetsum:
                self.f = True
            foo(r.left, pathsum)
            foo(r.right, pathsum)
        foo(root, 0)
        return self.f


# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)
# root.right.right.right.right = TreeNode(5)
# print(f'Result: {root.haspathsum(15)}')


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
print(f'Result: {root.haspathsum(-4)}')