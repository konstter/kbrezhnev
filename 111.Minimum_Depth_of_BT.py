# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def mindepth(self):
        self.min = 999999

        def foo(h, k):

            if h:
                k += 1
                if not h.left and not h.right:
                    self.min = min(self.min, k)
                return foo(h.left, k), foo(h.right, k)

        foo(root, 0)
        return self.min


# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)
# root.right.right.right.right = TreeNode(5)
# print(f'Result: {root.mindepth()}')


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(f'Result: {root.mindepth()}')

# root = TreeNode(1)
# root.left = TreeNode(2)
# print(f'Result: {root.mindepth()}')

root = TreeNode(-9)
root.left = TreeNode(-3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(-6)
root.left.right.right = TreeNode(0)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(-5)
root.right.right = TreeNode(0)
print(f'Result: {root.mindepth()}')