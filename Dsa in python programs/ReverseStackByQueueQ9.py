class Stack:
    def __init__(self):
        self.s = []
    def push(self, data):
        self.s.append(data)
    def pop(self):
        if not self.s:
            return None
        return self.s.pop()
    def display(self):
        print(self.s)

class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self, data):
        self.q.append(data)
    def dequeue(self):
        if not self.q:
            return None
        return self.q.pop(0)

def reverse_stack(stack):
    q = Queue()
    while stack.s:
        q.enqueue(stack.pop())
    while q.q:
        stack.push(q.dequeue())

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Original Stack:")
s.display()
reverse_stack(s)
print("Reversed Stack:")
s.display()