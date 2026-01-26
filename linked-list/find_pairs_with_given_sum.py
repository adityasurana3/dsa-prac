from typing import Optional


class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None
        self.prev = None


class FindPairs:
    def __init__(self, head: Optional[ListNode] = None):
        self.head = head

    def print_node(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def find_pairs(
            self, target: int, head: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        left = right = head
        result = []
        while right.next is not None:
            right = right.next
        while left is not None and right is not None and left.val < right.val:
            add_ = left.val + right.val
            if add_ == target:
                result.append((right.val, left.val))
                left = left.next
                right = right.prev
            elif add_ > target:
                right = right.prev
            else:
                left = left.next
        return result


dll1 = ListNode(1)
dll2 = ListNode(2)
dll3 = ListNode(4)
dll4 = ListNode(5)
dll5 = ListNode(6)
dll6 = ListNode(8)
dll7 = ListNode(9)

dll1.next = dll2
dll2.next = dll3
dll2.prev = dll1
dll3.next = dll4
dll3.prev = dll2
dll4.next = dll5
dll4.prev = dll3
dll5.next = dll6
dll5.prev = dll4
dll6.next = dll7
dll6.prev = dll5
dll7.next = None
dll7.prev = dll6

s = FindPairs(dll1)
results = s.find_pairs(7, dll1)
print(results)
s.print_node()
