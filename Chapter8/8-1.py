class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def empty(self) -> bool:
        return self.size == 0

    def max(self) -> int:
        if self.size > 0:
            return self.stack[-1][1]

    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()[0]

    def push(self, x: int) -> None:
        if self.size > 0:
            self.stack.append((x, max(x, self.max())))
        else:
            self.stack.append((x, x))
        self.size += 1

