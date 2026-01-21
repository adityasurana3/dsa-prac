from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_nodes(self, head: Optional[ListNode]) -> None:
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def remove_node(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        ######################## Brute force ###########################
        if not head:
            return None
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        if count == k:
            head = head.next
            return head
        pos = 1
        temp = head
        index_to_remove = count - k
        prev = None
        while pos <= count:
            print(pos <= count, temp is not None, temp.val, index_to_remove, pos)
            if index_to_remove == pos:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            pos += 1
        return head
        """
        if k <= 0:
            raise ValueError("k must be at least 1")

        slow = fast = head
        for _ in range(k):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


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
s.remove_node(node1, 1)
