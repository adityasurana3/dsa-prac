from typing import Optional, List


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ###################################### Brute-force approach (O(N)) ######################################
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        middle = count // 2

        temp = head
        for _ in range(middle):
            temp = temp.next

        return temp
        """

        # (O(N/2))
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


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
    [1, 2, 3, 4, 5, 6],
    [42],
    [1, 2],
    [],
]

s = Solution()
for i, case in enumerate(test_cases, 1):
    head = build_linked_list(case)
    middle_node = s.middleNode(head)
    result = linked_list_to_list(middle_node)
    print(f"Test Case {i}: Input: {case} → Output: {result}")
