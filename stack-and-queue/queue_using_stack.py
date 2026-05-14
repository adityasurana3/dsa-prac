from typing import List, Any


class QueueUsingStack:
    def __init__(self) -> None:
        self.stack1: List[Any] = []
        self.stack2: List[Any] = []

    def enqueue(self, val: Any) -> None:
        self.stack1.append(val)

    def dequeue(self) -> Any:
        if self.is_empty:
            print("Queue is empty")
            return -1

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def front(self) -> Any:
        if self.is_empty:
            print("Queue is empty")
            return -1

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def rear(self) -> Any:
        if self.is_empty:
            print("Queue is empty")
            return -1

        if self.stack1:
            return self.stack1[-1]

        return self.stack2[0]

    @property
    def is_empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    @property
    def size(self) -> int:
        return len(self.stack1) + len(self.stack2)

    def __repr__(self) -> str:
        queue_list = self.stack2[::-1] + self.stack1
        return f"QueueUsingStack({queue_list})"


queue = QueueUsingStack()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue)

print(queue.dequeue())

print(queue)

print(queue.front())

print(queue.rear())

print(queue.size)

print(queue.is_empty)
