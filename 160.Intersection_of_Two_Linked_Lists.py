# https://leetcode.com/problems/intersection-of-two-linked-lists/

def getintersectionnode(headA , headB):
    if headA == headB: return headA
    d = {}

    while headA:
        d[headA] = 1
        headA = headA.next

    while headB:
        if headB in d:
            return headB
        headB = headB.next

    return None




