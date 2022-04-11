class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.items = [None] * self.size

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|    |' + result
            else:
                result = f'\n| {item} |' + result
        return result

    def is_empty(self):
        return True if self.top == -1 else False

    def is_full(self):
        return True if self.top == self.size-1 else False

    def push(self, item):
        if self.is_full():
            raise Exception('it is full')
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception('it is empty')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def peek(self):
        if self.is_empty():
            raise Exception('it is empty')
        else:
            return self.items[self.top]