from typing import List, Union


class Stack:
    def __init__(self):
        self._result: List[int] = []

    def __repr__(self):
        return f"Stack({self._result})"

    def print_stack(self) -> None:
        print(self._result)

    def push(self, value) -> None:
        self._result.append(value)

    def pop(self) -> str | int:
        if len(self._result) == 0:
            return "Stack is empty"

        return self._result.pop()

    def top(self) -> Union[str, int]:
        if len(self._result) == 0:
            return "Stack is empty"

        return self._result[-1]

    @property
    def is_empty(self) -> bool:
        return len(self._result) == 0

    @property
    def size(self) -> int:
        return len(self._result)


stack = Stack()

stack.push(20)
stack.push(34)
stack.push(10)
stack.push(58)

print(stack)
print(stack.size)
print(stack.top())

removed_item = stack.pop()
print(removed_item)

print(stack)
print(stack.is_empty)
