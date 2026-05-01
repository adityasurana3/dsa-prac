from typing import Any, List

ALLOWED_TYPES = (int, float, str)


class _Node:
    def __init__(self, val) -> None:
        self.prev: "_Node | None" = None
        self._value = self._validate(val)
        self.next: "_Node | None" = None

    @property
    def value(self):
        return self._value

    @staticmethod
    def _validate(val):
        if val is None or not isinstance(val, ALLOWED_TYPES):
            raise TypeError(f"Value must be one of {ALLOWED_TYPES}, got {type(val)}")
        return val

    @value.setter
    def value(self, val):
        self._value = self._validate(val=val)


class QueueUsingLinkedList:
    def __init__(self) -> None:
        self.head: _Node | None = None
        self.tail: _Node | None = None

    def enqueue(self, val: int) -> None:
        node = _Node(val)
        print(node.value, "value")
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeue(self) -> int:
        if self.head is None:
            print("Queue is empty")
            return -1
        popped_item = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        return popped_item

    def front(self) -> int:
        if self.head is None:
            print("Queue is empty")
            return -1
        return self.head.value

    def rear(self) -> int:
        if self.head is None:
            print("Queue is empty")
            return -1
        return self.tail.value

    def __repr__(self) -> str:
        curr = self.head
        queue_list = []
        while curr is not None:
            queue_list.append(curr.value)
            curr = curr.next
        return f"QueueLinkedList({queue_list})"


queue = QueueUsingLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue)
print(queue.dequeue())

print(queue)

print(queue.front())
print(queue.rear())
