#https://leetcode.com/problems/reverse-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverselist(head):
    if not head: return
    nxt = prv = head.next
    head.next = None
    while nxt:
        nxt = nxt.next
        prv.next = head
        head = prv
        prv = nxt
    return head

if __name__ == "__main__":
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h = reverselist(h)
    while h:
        print(h.val)
        h = h.next

