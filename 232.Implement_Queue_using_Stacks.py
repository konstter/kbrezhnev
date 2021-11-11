# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        if self.empty():
            return None
        p = ''
        for i in self.s1:
            p += str(i) + ' '
        return p

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            self.s2 = self.s1[::-1]
            first = self.s2.pop()
            self.s1, self.s2 = self.s2[::-1], []
            return first

    def peek(self) -> int:
        if self.empty():
            return None
        else:
            self.s2 = self.s1[::-1]
            first = self.s2[-1]
            self.s1, self.s2 = self.s2[::-1], []
            return first

    def empty(self) -> bool:
        if self.s1:
            return False
        else:
            return True


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(-1)
    obj.push(3)
    obj.push(5)
    print(obj)
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())
    print(obj)

