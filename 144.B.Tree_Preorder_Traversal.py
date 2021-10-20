# https://leetcode.com/problems/binary-tree-preorder-traversal/
class TreeNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def preordertraversal(root):
    if not root: return []
    res = []

    def foo(r):
        if not r: return
        res.append(r.val)
        foo(r.left)
        foo(r.right)
    foo(root)

    return res

if __name__== '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(preordertraversal(root))