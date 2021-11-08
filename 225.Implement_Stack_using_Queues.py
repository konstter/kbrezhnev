# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        if self.empty():
            self.q1 = self.q2
        else:
            for i in self.q1:
                self.q2.append(i)
            self.q1 = self.q2
        self.q2 = []

    def pop(self) -> int:
        if self.empty():
            return
        else:
            res = self.q1[0]
            self.q1 = self.q1[1:]
            return res

    def top(self) -> int:
        if self.empty():
            return
        else:
            return self.q1[0]

    def empty(self) -> bool:
        if self.q1:
            return False
        else:
            return True


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())
    print(myStack.pop())
    print(myStack.empty())
