class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class DLL:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp=temp.next
                
    def insert_beginning(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
        
    def insert_end(self,data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
       
    def insert_pos(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n         
        
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
        
    def delete_end(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None
        
    def delete_pos(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None
        
        
dll=DLL()
n1=Node(10)
dll.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n3.prev=n2
n2.next=n3
n4=Node(40)
n4.prev=n3
n3.next=n4
dll.insert_beginning(5)
dll.insert_end(50)
dll.insert_pos(3,25)
dll.delete_beginning()
dll.delete_end()
dll.delete_pos(2)
dll.display()