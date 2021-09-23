class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def node_insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.node_insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.node_insert(val)
        else:
            self.val = val

    def from_list(self, l):
        for i in range(1, len(l)):
            self.node_insert(l[i])


def issametree(p, q):
    if not p and not q:
        return True
    s1, s2 = [], []
    while True:
        if p and q:
            if p.val != q.val:
                return False
            else:
                s1.append(p)
                s2.append(q)
                p, q = p.left, q.left
        elif not p and not q and s1 and s2:
            item1, item2 = s1.pop(), s2.pop()
            p, q = item1.right, item2.right
        elif not p and not q and not s1 and not s2:
            return True
        else:
            return False



l1 = [1, 0, 2, 3]
l2 = [1, 0, 2, 1]
root1 = TreeNode(l1[0])
TreeNode.from_list(root1, l1)
root2 = TreeNode(l2[0])
TreeNode.from_list(root2, l2)

print(issametree(root1, root2))