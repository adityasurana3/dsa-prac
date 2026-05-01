class Node:
    def __init__(self, val):
        self.prev = None
        self.value = val
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return -1
        popped_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_value

    def top(self):
        if self.head is None:
            print("Stack is empty")
            return -1
        return self.tail.value

    def print_stack(self):
        curr = self.head
        stack_list = []
        while curr is not None:
            stack_list.append(curr.value)
            curr = curr.next
        print(stack_list)

    def __repr__(self):
        curr = self.head
        stack_list = []
        while curr is not None:
            stack_list.append(curr.value)
            curr = curr.next
        return f"StackLinkedList({stack_list})"


stack = StackUsingLinkedList()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.pop()

print(stack.top())

print(stack)
