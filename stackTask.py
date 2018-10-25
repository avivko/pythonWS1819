class Stack:

    def __init__(self):
        self._stack = []

    def is_empty(self):
        if not self._stack:
            return True
        return False

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        self._stack.pop()

    def peek(self):
        if not self.is_empty():
            return self._stack[len(self._stack) - 1]
        return self._stack


def main():
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    print(stack.is_empty())


if __name__ == '__main__':
    main()
