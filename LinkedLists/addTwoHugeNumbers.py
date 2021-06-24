# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    a_str = ""
    b_str = ""
    
    node = a
    while node:
        temp = str(node.value)
        while len(temp) < 4:
            temp = "0" + temp
        a_str += temp
        node = node.next

    node = b
    while node:
        temp = str(node.value)
        while len(temp) < 4:
            temp = "0" + temp
        b_str += temp
        node = node.next
        
    combined = str(int(a_str) + int(b_str))
    if combined == "0":
        return [0]
    
    res = []
    temp = ""
    for i in combined:
        temp += i
        if len(temp) == 4:
            if temp == "0000" or temp == "000" or temp == "00" or temp == "0":
                temp = "0"
            elif temp[0] == "0":
                temp = temp[1:len(temp)]
            else:
                while int(temp) % 10 == 0:
                    temp = str(int(temp) // 10)
            res.append(int(temp))
            temp = ""
            
    if temp != "":
        res.append(int(temp))
    
    return res