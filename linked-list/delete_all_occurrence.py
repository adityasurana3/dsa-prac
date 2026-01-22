from typing import Optional


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None
        self.prev = None


class DeleteAllOccurrence:
    def __init__(self, head: Optional[ListNode] = None):
        self.head = head

    def print_node(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def delete_occurrence(
        self, key: int, head: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        if self.head.next is None or self.head.val == key:
            return None

        temp = self.head
        prev = None
        new_head = head
        while temp is not None:
            if temp.val == key:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
            prev = temp
            temp = temp.next
        return new_head


dll1 = ListNode(5)
dll2 = ListNode(2)
dll3 = ListNode(3)
dll4 = ListNode(2)
dll5 = ListNode(10)

dll1.next = dll2
dll2.next = dll3
dll2.prev = dll1
dll3.next = dll4
dll3.prev = dll2
dll4.next = dll5
dll4.prev = dll3
dll5.next = None
dll5.prev = dll4


s = DeleteAllOccurrence(dll1)
s.delete_occurrence(2, dll1)
s.print_node()
