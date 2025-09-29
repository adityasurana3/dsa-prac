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
        my_dict = {}
        count = 0
        while temp is not None:
            if temp in my_dict:
                return count - my_dict[temp]
            my_dict[temp] = count
            temp = temp.next
            count += 1
        return 0
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0
