from contextlib import nullcontext


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head.next:
            return 0 if head.val == 0 else 1
        buffer = []
        total = 0
        while head:
            buffer.insert(0, head.val)
            head = head.next
        for i in range(len(buffer)):
            total += pow(2, i) if buffer[i] == 1 else 0
        return total