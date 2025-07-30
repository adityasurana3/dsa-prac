class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if not self.head:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end=" ")
                curr = curr.next

    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_element = None
            count = 0
            current = self.head

            while current is not None and count < position:
                prev_element = current
                current = current.next
                count += 1
            prev_element.next = new_node
            new_node.next = current

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        if temp.value == value:
            self.head = temp.next
            return
        prev = None
        while temp is not None:
            if temp.value == value:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print("Node not found")
        else:
            prev.next = temp.next

    def __str__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return " -> ".join(values) if values else "Empty List"


def run_tests():
    print("Test Case 1: Delete from empty list")
    sll = SinglyLinkedList()
    sll.delete(10)

    print("\nTest Case 2: Delete head node")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("Before delete:", sll)
    sll.delete(10)
    print("After delete:", sll)

    print("\nTest Case 3: Delete middle node")
    sll.delete(20)
    print("After delete:", sll)

    print("\nTest Case 4: Delete last node (tail)")
    sll.delete(30)
    print("After delete:", sll)

    print("\nTest Case 5: Delete node not found")
    sll.append(5)
    sll.append(15)
    print("Before delete:", sll)
    sll.delete(100)
    print("After delete:", sll)

    print("\nTest Case 6: Multiple deletions")
    sll.delete(5)
    sll.delete(15)
    print("After all deletions:", sll)

    print("\nTest Case 7: Delete from single-node list")
    sll.append(99)
    print("Before delete:", sll)
    sll.delete(99)
    print("After delete:", sll)


if __name__ == "__main__":
    run_tests()
