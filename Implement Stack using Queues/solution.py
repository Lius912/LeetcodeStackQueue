class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.size += 1

    def pop(self):
        if not self.head:
            raise IndexError()
        temp = self.head.data
        if self.head is self.tail:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
        self.size -= 1
        return temp

    def peek(self):
        if not self.head:
            raise IndexError()
        return self.head.data

    def empty(self) -> bool:
        return self.head is None

class MyStack:
    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        self.stack.push(x)
        if self.stack.size > 1:
            for _ in range(self.stack.size - 1):
                self.stack.push(self.stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack.peek()

    def empty(self) -> bool:
        return self.stack.empty()
        