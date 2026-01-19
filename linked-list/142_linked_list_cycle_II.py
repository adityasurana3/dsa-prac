from typing import Optional, List


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ######################## Brute force ###########################
        temp = head
        node = set()
        while temp is not None:
            if temp in node:
                return temp
            node.add(temp)
            temp = temp.next
        return None
        """
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    
