class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def __init__(self):
        self.head=None
    
    def insert_beginning(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
        
    def insert_end(self,data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
    
    def insert_pos(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        n.data=data
        n.next=temp.next
        temp.next=n
        
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_pos(self,pos):
         prev=self.head
         temp=self.head.next
         for i in range(pos-1):
             temp=temp.next
             prev=prev.next
         prev.next=temp.next
    
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp=temp.next
            
sll=SLL()
n1=Node(10)
sll.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
sll.insert_beginning(5)
sll.insert_end(40)
sll.insert_pos(3,25)
sll.delete_beginning()
sll.delete_end()
sll.delete_pos(2)
sll.display()
