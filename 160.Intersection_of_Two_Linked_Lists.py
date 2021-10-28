# https://leetcode.com/problems/intersection-of-two-linked-lists/

def lengthoglist(head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l

def newhead(head, delta):
    while delta != 0:
        head = head.next
        delta -= 1
    return head

def getintersectionnode(headA , headB):
    if headA == headB: return headA
    hA, hB = headA, headB
    a, b = lengthoglist(headA), lengthoglist(headB)
    if a > b:
        hA = newhead(headA, abs(a-b))
    elif b > a:
        hB = newhead(headB, abs(a-b))

    while hA:
        if hA == hB:
            return hA
        hA = hA.next
        hB = hB.next

    return None





