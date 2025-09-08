from typing import Optional, List


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ############## Brute force ####################
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next
        return head
        """
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


test_cases = [
    [1, 2, 3, 4, 5],
    # [1, 2, 3, 4, 5, 6],
    # [42],
    # [1, 2],
    # [],
]

s = Solution()
for i, case in enumerate(test_cases, 1):
    head = build_linked_list(case)
    middle_node = s.reverseList(head)
    result = linked_list_to_list(middle_node)
    print(f"Test Case {i}: Input: {case} → Output: {result}")
