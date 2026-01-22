from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def __init__(self, head):
        self.head = head

    def print_node(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def reverseList(self, head: Optional[ListNode] = None) -> Optional[ListNode]:
        if self.head is None:
            return head
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            temp.prev = front
            prev = temp
            temp = front
        self.head = prev
        self.print_node()
        return self.head


dll1 = ListNode(6)
dll2 = ListNode(4)
dll3 = ListNode(7)
dll4 = ListNode(1)

dll1.next = dll2
dll2.next = dll3
dll2.prev = dll1
dll3.next = dll4
dll3.prev = dll2
dll4.prev = dll3
dll4.next = None

s = Solution(dll1)
s.reverseList()
