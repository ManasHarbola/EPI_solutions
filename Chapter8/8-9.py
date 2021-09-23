class Queue:
    def __init__(self):
        self.insertion_stack, self.removal_stack = [], []
    def enqueue(self, x: int) -> None:
        self.insertion_stack.append(x)
    def dequeue(self) -> int:
        if not self.removal_stack:
            while self.insertion_stack:
                self.removal_stack.append(self.insertion_stack.pop())
        return self.removal_stack.pop()

