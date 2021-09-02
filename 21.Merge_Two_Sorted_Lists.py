#https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def lst2link(lst):
    link = head = ListNode(lst[0], lst[1])
    for e in range(1, len(lst)):
        link.next = ListNode(lst[e])
        link = link.next
    return head

def mergetwolists(l1, l2):
    if not l1 and not l2:
        return None
    elif not l1:
        res = h = ListNode(l2.val)
        l2 = l2.next
    elif not l2:
        res = h = ListNode(l1.val)
        l1 = l1.next
    else:
        if l1.val <= l2.val:
            res = h = ListNode(l1.val)
            l1 = l1.next
        else:
            res = h = ListNode(l2.val)
            l2 = l2.next
    while l1 or l2:
        if l1 and l2:
            if l1.val <= l2.val:
                res.next = ListNode(l1.val)
                res = res.next
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next
        elif not l1:
            res.next = ListNode(l2.val)
            res = res.next
            l2 = l2.next
        else:
            res.next = ListNode(l1.val)
            res = res.next
            l1 = l1.next
    return h

l1 = lst2link([1, 2, 3])
l2 = lst2link([3, 4, 5])

r = mergetwolists(l1, l2)

while r.next:
    print(r.val)
    r = r.next
