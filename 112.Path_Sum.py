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

root = TreeNode(1)
root.left = TreeNode(-2)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(-1)
root.left.right = TreeNode(3)
root.right = TreeNode(-3)
root.right.left = TreeNode(-2)
print(f'Result: {root.haspathsum(-4)}')