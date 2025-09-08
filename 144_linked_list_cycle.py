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
                return True
            node.add(temp)
            temp = temp.next
        return False
        """
        first_pointer = head
        second_pointer = head
        while first_pointer is not None and first_pointer.next is not None:
            first_pointer = first_pointer.next.next
            second_pointer = second_pointer.next
            if first_pointer == second_pointer:
                return True
        return False
