class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        n = Node(data)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            val = self.top.data
            self.top = self.top.next
            return val

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            return self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

print("Stack Using Linked List")
s = StackLL()
s.push(10)
s.push(20)
s.push(30)
print("After Push")
s.display()
print("Peek:", s.peek())
print("Popped:", s.pop())
print("After Pop")
s.display()