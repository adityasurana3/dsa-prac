import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ######################## Brute force ###########################
        if not head:
            return None
        list_node = []
        temp = head
        while temp is not None and temp.next is not None:
            list_node.append(temp.val)
            temp = temp.next.next
        if temp:
            list_node.append(temp.val)
        temp = head.next
        while temp is not None and temp.next is not None:
            list_node.append(temp.val)
            temp = temp.next.next
        temp = head
        for i in list_node:
            temp.val = i
            temp = temp.next
        return head
        """
        if head is None:
            return head

        odd = head
        even = head.next
        even_head = even
        while even and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head


node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node7 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None


s = Solution()
s.oddEvenList(node1)
