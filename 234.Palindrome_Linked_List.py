# https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ispalindrome(head):
    if not head or not head.next: return True
    fast = slow = prev_slow = head
    while fast and fast.next:
        if slow != head:
            slow = slow.next
            prev_slow.next = head
            head, prev_slow = prev_slow, slow
        else:
            slow, prev_slow = slow.next, prev_slow.next
            # head.next = None
        fast = fast.next.next

    if head.next == slow:
        head.next = None

    if fast:
        slow = slow.next

    while slow:
        if head.val != slow.val:
            return False
        head = head.next
        slow = slow.next

    return True


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(1)
    # h.next.next = ListNode(1)
    # h.next.next.next = ListNode(1)
    # h.next.next.next.next = ListNode(1)
    # h.next.next.next.next.next = ListNode(1)
    # h.next.next.next.next.next.next = ListNode(1)
    print(ispalindrome(h))
