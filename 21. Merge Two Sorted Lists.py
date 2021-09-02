# https://leetcode.com/problems/merge-two-sorted-lists/

# Traceback (most recent call last):
# File "C:\temp\py\sqlite\21. Merge Two Sorted Lists.py", line 44, in <module>
# print(mergetwolists(k1, n1))
# File "C:\temp\py\sqlite\21. Merge Two Sorted Lists.py", line 23, in mergetwolists
# res.append(elem1.val)
# AttributeError: 'int' object has no attribute 'val'

class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n


def lst2link(lst):
    link = head = ListNode(lst[0], lst[1])
    for e in range(1, len(lst)):
        link.next = ListNode(lst[e])
        link = link.next
    return head.next


def mergetwolists(elem1, elem2):
    res = []
    while elem1 or elem2:
        if elem1 and elem2:
            res.append(elem1.val)
            res.append(elem2.val)
            elem1 = elem1.next
            elem2 = elem2.next
        elif not elem1:
            res.append(elem2.val)
            elem2 = elem2.next
        elif not elem2:
            res.append(elem1.val)
            elem1 = elem1.next
    res.sort()
    return lst2link(res)



n1 = ListNode(1, 2)
n2 = ListNode(2, 3)
n3 = ListNode(3)
k1 = ListNode(4, 5)
k2 = ListNode(5, 6)
k3 = ListNode(6)
print(mergetwolists(k1, n1))
