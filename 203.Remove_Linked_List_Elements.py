# https://leetcode.com/problems/remove-linked-list-elements/

def removeelements(head, val):
    if not head: return None
    node = head
    prev = None
    while node:
        if node.val == val:
            if prev == None:
                node = node.next
                head = node
            else:
                node = node.next
                prev.next = node
        else:
            prev = node
            node = node.next
    return head

