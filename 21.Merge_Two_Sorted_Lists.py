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
    if not l1 or not l2: return l1 or l2
    h1, h2 = l1, l2
    h_res = None
    res = None

    while h1 and h2:
        if h1.val < h2.val:
            tmp = h1.val
            h1 = h1.next
        else:
            tmp = h2.val
            h2 = h2.next

        if not res:
            res = ListNode(tmp)
            h_res = res
        else:
            res.next = ListNode(tmp)
            res = res.next
    res.next = h1 or h2
    return h_res

l1 = lst2link([1, 2, 3])
l2 = lst2link([3, 4, 5])

r = mergetwolists(l1, l2)

while r.next:
    print(r.val)
    r = r.next
