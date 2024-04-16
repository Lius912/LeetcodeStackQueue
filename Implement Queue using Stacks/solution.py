class Node:
    def __init__(self, data, prev: int = None):
        self.data = data
        self.prev = prev

    def __str__(self):
        return f"{self.prev} -> {self.data}"

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        if not self.top:
            self.top = Node(val)
        else:
            self.top = Node(val, self.top)
        self.size += 1

    def peek(self):
        if not self.top:
            raise IndexError()
        return self.top.data

    def pop(self):
        if not self.top:
            raise IndexError()
        temp = self.top.data
        self.top = self.top.prev
        self.size -= 1
        return temp

    def empty(self):
        return self.size == 0

    def __repr__(self):
        return f"{self.top}"

class MyQueue:
    def __init__(self):
        self.head = Stack()
        

    def push(self, x: int) -> None:
        if self.size() == 0:
            self.head.push(x)
        else:
            new_stack = Stack()
            for _ in range(self.head.size):
                new_stack.push(self.head.pop())
            self.head.push(x)
            for _ in range(new_stack.size):
                self.head.push(new_stack.pop())

    def pop(self) -> int:
        return self.head.pop()

    def peek(self) -> int:
        return self.head.peek()

    def size(self):
        return self.head.size


    def empty(self) -> bool:
        return self.head.empty()

    def __repr__(self):
        return repr(self.head)
