class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        n = Node(data)
        temp = self.head
        if temp is None:
            self.head = n
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

def reverse_singly(sll):
    prev = None
    current = sll.head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    sll.head = prev

class Node1:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        n = Node1(data)
        temp = self.head
        if temp is None:
            self.head = n
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.prev = temp

    def display(self):
        if self.head is None:
            print("Circular linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

def reverse_doubly(dll):
    current = dll.head
    temp = None
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp:
        dll.head = temp.prev

print("Singly")
sll = SLL()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)
print("Original")
sll.display()
reverse_singly(sll)
print("Reversed")
sll.display()

print("\nDoubly")
dll = DLL()
dll.insert_end(11)
dll.insert_end(22)
dll.insert_end(33)
print("Original")
dll.display()
reverse_doubly(dll)
print("Reversed")
dll.display()