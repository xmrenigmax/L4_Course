#stack data structure
## last in first out

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display_info(self):
        print("Stack:", self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.size())
stack.display_info()