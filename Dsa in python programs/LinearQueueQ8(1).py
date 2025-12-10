class LinearQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        if not self.q:
            print("Queue is empty")
        else:
            return self.q.pop(0)

    def display(self):
        print(self.q)

q = LinearQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()

