class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.outstack:
            self.in2out()
        return self.outstack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outstack:
            self.in2out()
        return self.outstack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.instack and not self.outstack

    def in2out(self):
        while self.instack:
            self.outstack.append(self.instack.pop())