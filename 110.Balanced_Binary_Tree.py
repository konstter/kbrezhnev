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


def isbalanced(root):
    if not root: return True

    res = [0, 0]
    r = [root.left, root.right]
    for i in range(2):
        def foo(node):
            if not node: return 0
            return max(foo(node.left), foo(node.right)) + 1
        res[i] = foo(r[i])
    if (abs(res[0] - res[1]) <= 1) and isbalanced(root.left) and isbalanced(root.right):
        return True
    return False


    # if not root: return 0
    #
    # def foo(node, k):
    #     if not node:
    #         print(k)
    #         return k
    #     k += 1
    #     foo(node.left, k)
    #     foo(node.right, k)
    # l = foo(root.left, 0)
    # r = foo(root.right, 0)
    # return abs(l - r) <= 1


l = [1, 0, 2, 1]
root = TreeNode(l[0])
TreeNode.from_list(root, l)

print(isbalanced(root))




