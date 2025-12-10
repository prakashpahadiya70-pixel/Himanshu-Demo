class StackArray:
    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, data):
        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            return self.stack.pop()

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i], end=" -> ")
            print("None")


print("Stack Using Array")

s = StackArray(5)
s.push(10)
s.push(20)
s.push(30)

print("After Push")
s.display()

print("Popped:", s.pop())

print("After Pop")
s.display()
