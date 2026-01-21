from typing import Any, Iterator, Iterable, Optional


class Node:
    __slots__ = ("val", "next", "prev")

    def __init__(self, val: Any):
        self.val: Any = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.val!r})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        return f"DoublyLinkedList([{', '.join(map(repr, self))}])"

    def insert_at_head(self, val: Any) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val: Any) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at(self, val: Any, position: int) -> None:
        new_node = Node(val=val)
        if position == 0:
            self.insert_at_head(val)
            return
        current = self.head
        count = 0
        while current.next and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position Out of bound")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def traverse(self):
        values = []
        if not self.head:
            return None
        current = self.head
        while current is not None:
            values.append(current.val)
            print(current.val, end=" ")
            current = current.next
        return values

    def delete_head(self) -> None:
        if not self.head:
            print("List is empty")
            raise IndexError("Delete from empty list")
        if not self.head.next:
            self.head = None
            return None
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        if not self.head:
            print("List is empty")
            raise IndexError("Delete from empty list")
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.prev.next = None

    def delete_in_between(self, position: int) -> None:
        if not self.head:
            raise IndexError("Delete from empty list")
        if position == 0:
            self.delete_head()
            return
        curr = self.head
        count = 0
        while curr is not None and count < position:
            curr = curr.next
            count += 1
        if not curr:
            print("Position out of bound")
            raise IndexError("Index out of range")
        if not curr.next:
            curr.prev.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
