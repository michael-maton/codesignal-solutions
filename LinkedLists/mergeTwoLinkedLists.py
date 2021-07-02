# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
        
    c1 = l1
    c2 = l2
    current = ListNode(None)
    combined = current
    while c1 and c2:
        if c1.value <= c2.value:
            combined.next = c1
            c1 = c1.next
        else:
            combined.next = c2
            c2 = c2.next
        
        combined = combined.next
        
    if c1:
        combined.next = c1
    elif c2:
        combined.next = c2
        
    
    return current.next
