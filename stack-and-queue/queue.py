from typing import List, Union


class Queue:
    def __init__(self):
        self._result: List[int] = []

    def __repr__(self):
        return f"Queue({self._result})"

    def print_queue(self) -> None:
        print(self._result)

    def enqueue(self, value) -> None:
        self._result.append(value)

    def dequeue(self) -> str | int:
        if len(self._result) == 0:
            return "Queue is empty"
        r = self._result.pop(0)
        return r

    def front(self) -> Union[str, int]:
        if len(self._result) == 0:
            return "Queue is empty"
        return self._result[0]

    def rear(self) -> Union[str, int]:
        if len(self._result) == 0:
            return "Queue is empty"
        return self._result[-1]

    @property
    def is_empty(self) -> bool:
        return len(self._result) == 0

    @property
    def size(self) -> int:
        return len(self._result)


queue = Queue()

queue.enqueue(20)
queue.enqueue(34)
queue.enqueue(10)
queue.enqueue(58)

print(queue)
print(queue.size)
print(queue.front())
print(queue.rear())

removed_item = queue.dequeue()
print(removed_item)

print(queue)
print(queue.is_empty)
