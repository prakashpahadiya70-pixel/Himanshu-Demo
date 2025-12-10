class node: 
    def __init__(self,val): 
        self.lchild=None 
        self.data=val 
        self.rchild=None 
class btree: 
    def __init__(self): 
        self.root=None 
    def insert(self,val): 
        temp=node(val) 
        trv=self.root 
        if self.root is None: 
            self.root=temp 
            return 
        else: 
            while True: 
                if(val > trv.data): 
                    if trv.rchild is None: 
                        trv.rchild=temp 
                        return 
                    else: 
                        trv=trv.rchild 
                else: 
                    if trv.lchild is None: 
                        trv.lchild=temp 
                        return 
                    else: 
                        trv=trv.lchild 
    
    def search(self,key): 
        trv=self.root 
        while True: 
            if trv is None: 
                return False 
            if trv.data==key: 
                return True 
            if trv.data<key: 
                trv=trv.rchild 
            else: 
                trv=trv.lchild 
             
    def searchR(self, root, key): 
        if root is None: 
            return False 
        elif key < root.data: 
            return self.search(root.lchild,key) 
        elif key > root.data: 
            return self.search(root.rchild,key) 
        else: 
            if root.data==key: 
                return True 
            else: 
                return False 
     
    def inorder(self,rt): 
        if rt is not None: 
            self.inorder(rt.lchild) 
            print(rt.data,end=" ") 
            self.inorder(rt.rchild) 
    def preorder(self,rt): 
        if rt is not None: 
            print(rt.data,end=" ") 
            self.preorder(rt.lchild) 
            self.preorder(rt.rchild)   
    def postorder(self,rt): 
        if rt is not None: 
            self.postorder(rt.lchild) 
            self.postorder(rt.rchild) 
            print(rt.data,end=" ") 
    def inorder_traversal(self): 
        stack = [] 
        current = self.root 
        result = [] 
        while current or stack: 
            while current: 
                stack.append(current) 
                current = current.lchild 
            current = stack.pop() 
            result.append(current.data) 
            current = current.rchild 
        return result 
    def preorder_traversal(self): 
        if not self.root: 
            return [] 
        stack, result = [self.root], [] 
        while stack: 
            node = stack.pop() 
            result.append(node.data) 
 
        # Push right child first so that left is processed first 
            if node.rchild: 
                stack.append(node.rchild) 
            if node.lchild: 
                stack.append(node.lchild) 
 
        return result 
    def post_order_traversal(self): 
        if self.root is None: 
            return [] 
 
        stack1 = [] 
        stack2 = [] 
        stack1.append(self.root) 
 
        while stack1: 
            node = stack1.pop() 
            stack2.append(node) 
 
            if node.lchild: 
                stack1.append(node.lchild) 
            if node.rchild: 
                stack1.append(node.rchild) 
 
        result = [] 
        while stack2: 
            node = stack2.pop() 
            result.append(node.data) 
 
        return result 
     
bst=btree() 
bst.insert(10) 
bst.insert(5) 
bst.insert(20) 
bst.insert(50) 
bst.insert(30) 
bst.insert(40) 
bst.insert(35) 
print("Inorder") 
#print(bst.inorder_traversal()) 
bst.inorder(bst.root) 
#bst.displayInorder() 
print("\nPreorder") 
#print(bst.preorder_traversal()) 
bst.preorder(bst.root) 
print("\nPostorder") 
#print(bst.post_order_traversal()) 
bst.postorder(bst.root) 
print("\nSearch for 10 in the BST:", bst.search(10)) 