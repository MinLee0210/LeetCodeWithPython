from typing import Optional


class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next
        
def merge(list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None: return
    if list2 is None: return 
    
    head = ListNode()
    tail = ListNode()
    
    # Initial the first value for the merge list.
    if list1.val < list2.val:
        head = tail = list1
        list1 = list1.next
    else:
        head = tail = list2
        list2 = list2.next
    
    # Start comparing
    while (list1.next != None) or (list2.next != None):
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
            
    # If there were a list finish sooner, we start to complete the merge list with the lefted.
    if list1 != None: 
        tail.next = list1
    else:
        tail.next = list2 
        
    return head