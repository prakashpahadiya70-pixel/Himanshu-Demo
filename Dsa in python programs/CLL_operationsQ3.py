class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def display(self):
        if self.head is None:
            print("Circular linked list is empty")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
            
    def add_begin(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            new.next=self.head
            self.tail.next=new
            self.head=new
                
    def add_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
                
    def add_position(self,pos,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            if pos==0:
                cll.add_begin(data)
            else:
                temp=self.head
                for i in range(pos-1):
                    temp=temp.next
                new.next=temp.next
                temp.next=new
                    
    def delete_begin(self):
        if self.head is None:
            print("No node in CLL")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                self.head=temp.next
                temp=None
                self.tail.next=self.head
                    
    def delete_end(self):
        if self.head is None:
            print("No node in CLL")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                while temp.next!=self.tail:
                    temp=temp.next
                self.tail=None
                self.tail=temp
                temp.next=self.head
                    
    def delete_pos(self,pos):
        if self.head is None:
            print("No node in CLL")
        elif pos==0:
            cll.add_begin()       
        else:
            temp1=self.head
            temp2=self.head.next
            for i in range(pos-1):
                temp1=temp1.next
                temp2=temp2.next
                temp1.next=temp2.next
                if temp2==self.tail:
                    self.tail=temp1
                temp2=None
                    
cll=CLL()
cll.add_begin(10)
cll.add_begin(20)
cll.add_begin(30)
cll.add_end(5)
cll.add_position(2,15)
cll.add_position(0,40)
cll.delete_begin()
cll.display()
cll.delete_end()
cll.display()
cll.delete_pos(2)
cll.display()
