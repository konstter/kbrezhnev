# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val):
        self.minstack.append(val)

    def pop(self):
        self.minstack.pop()

    def top(self):
        return self.minstack[-1]

    def getmin(self):
        return min(self.minstack)


if __name__ ==  '__main__':
    m = MinStack()
    m.push(-3)
    m.push(0)
    m.push(2)
    print(m.pop())
    print(m.top())
    print(m.getmin())