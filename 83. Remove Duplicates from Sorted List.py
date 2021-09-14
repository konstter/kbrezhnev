# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

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

def deleteduplicates(head):
    if not head: return head
    n = head
    while n.next:
        if n.val == n.next.val:
            n.val = n.next.val
            n.next = n.next.next
        else:
            n = n.next
    return head

l = lst2link([1, 1, 2, 2, 3])

r = deleteduplicates(l)


while r:
    print(r.val)
    r = r.next
