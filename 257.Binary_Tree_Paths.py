# https://leetcode.com/problems/binary-tree-paths/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binarytreepaths(root):
    path_list, path = [], ''

    def foo(r, pl, p):
        if r:
            if not r.left and not r.right:
                pl.append(p + str(r.val))
                p = ''
            p += str(r.val) + '->'
            foo(r.left, pl, p)
            foo(r.right, pl, p)
    foo(root, path_list, path)
    return path_list


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(2)
    print(binarytreepaths(root))