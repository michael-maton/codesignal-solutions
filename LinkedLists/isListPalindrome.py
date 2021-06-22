# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if l == None:
        return True
        
    # traverse to end of linked list and store values in stack
    node = l
    count = 0
    node_stack = []
    while node:
        count += 1
        node_stack.append(node.value)
        node = node.next
    
    # traverse list again, comparing list values to popped stack values
    node = l
    while node:
        top = node_stack.pop()
        
        if top != node.value:
            return False
        
        node = node.next
            
    return True
