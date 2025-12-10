stack = []

def push():
    item = input("Enter element to push: ")
    stack.append(item)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty!")
    else:
        stack.pop()
        print(stack)

while True:
    ch = int(input("\n1 Push\n2 Pop\n3 Exit\nEnter choice: "))
    if ch == 1: push()
    elif ch == 2: pop()
    else: break