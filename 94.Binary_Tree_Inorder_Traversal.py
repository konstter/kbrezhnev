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


def inordertraversal(root):
    if not root: return []
    s = []
    res = []
    while True:
        if not root and s:
            item = s.pop()
            res.append(item.val)
            root = item.right
        else:
            s.append(root)
            root = root.left
        if not root and not s:
            return res



l = [1, 0, 2, 3]
root = TreeNode(l[0])
TreeNode.from_list(root, l)

print(inordertraversal(root))


