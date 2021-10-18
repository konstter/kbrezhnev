# https://leetcode.com/problems/linked-list-cycle/

def hascycle(head):
    if not head: return False
    while True:
        if not head.next:
            return False
        head.val = 'passed'
        head = head.next
        if head.val == 'passed':
            return True