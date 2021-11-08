# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inverttree(root):
    ro = root

    def foo(root):
        if not root: return
        if root:
            k, root.left = root.left, root.right
            root.right = k
            foo(root.left)
            foo(root.right)
    foo(root)
    return ro

def printtree(root):
    if not root: print('None')
    l = []

    def bar(root):
        if root:
            l.append(root.val)
            bar(root.left)
            bar(root.right)
    bar(root)
    print(l)

if __name__ == '__main__':
    r = TreeNode(4)
    r.left = TreeNode(2)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(3)
    r.right = TreeNode(7)
    r.right.left = TreeNode(6)
    r.right.right = TreeNode(9)
    printtree(inverttree(r))