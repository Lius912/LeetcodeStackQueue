class Node:
    def __init__(self, data, nxt = None):
        self.data = data
        self.next = nxt
        self.freq = 1

    def final_data(self):
        return f"[{self.data.final_data() if isinstance(self.data, Node) else self.data}]"

    def show(self):
        return f"{self.final_data()} -> {self.next.show() if self.next else None}"

    def __repr__(self) -> str:
        return f"[{self.final_data()} -> {self.next.show() if self.next else None}]"

class FreqStack:
    def __init__(self):
        self.head = None
        self.max_val = 0

    def push(self, val: int) -> None:
        if not self.head:
            self.max_val = 1
            self.head = Node(val)
        else:
            node = self.head
            self.head = Node(val, self.head)
            while node:
                if node.data == val:
                    self.head.freq += node.freq
                    if self.head.freq > self.max_val:
                        self.max_val = self.head.freq
                    break
                node = node.next


    def pop(self) -> int:
        prev_node = None
        node = self.head
        while node:
            if node.freq == self.max_val:
                before_max_node = prev_node
                break
            prev_node = node
            node = node.next
        else:
            self.max_val -= 1
            prev_node = None
            node = self.head
            while node:
                if node.freq == self.max_val:
                    before_max_node = prev_node
                    break
                prev_node = node
                node = node.next
        if before_max_node is None:
            most_freq_val = self.head.data
            self.head = self.head.next
        else:
            most_freq_val = before_max_node.next.data
            before_max_node.next = before_max_node.next.next
        return most_freq_val

    def __repr__(self) -> str:
        return repr(self.head)