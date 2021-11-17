# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

def lowestcommonancestor(root, p, q):
    if not root: return

    if p.val < root.val and q.val < root.val:
        return lowestcommonancestor(root.left, p, q)

    if p.val > root.val and q.val > root.val:
        return lowestcommonancestor(root.right, p, q)

    return root


if __name__ == '__main__':
    p = r = TreeNode(2)
    q = r.left = TreeNode(1)
    print(lowestcommonancestor(r, p, q))
