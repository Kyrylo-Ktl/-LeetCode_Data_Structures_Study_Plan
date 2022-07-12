class MyQueue:
    """
    Time:
        push  O(1)
        pop   O(1)
        peek  O(1)
        empty O(1)
    Memory: O(n)
    """

    def __init__(self):
        self.stack = []
        self.out = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        self._move_out()
        return self.out.pop()

    def peek(self) -> int:
        self._move_out()
        return self.out[-1]

    def empty(self) -> bool:
        return not self.stack and not self.out

    def _move_out(self):
        if not self.out:
            while self.stack:
                self.out.append(self.stack.pop())
