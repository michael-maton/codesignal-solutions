class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def removeKFromList(l, k):
    # handles empty linked list
    if l == None:
        return l
        
    # gets rid of first value if it equals k
    elif l.value == k:
        l = l.next
    
    
    current = l
  
    while current is not None and current.next is not None:
        if current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
            
    if current is not None and current.value == k:
        l = l.next
            
    return l

def removeKFromList2(l, k):
    current = l
    prev = None
    
    while current is not None:
        if prev == None:
            if current.value == k:
                l = current.next
                current = l
            else:
                prev = current
                current = current.next
        else:
            if current.value == k:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
            
    return l

