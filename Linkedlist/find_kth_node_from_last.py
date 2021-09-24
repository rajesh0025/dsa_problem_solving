class Node:
    def __init__(self, info, link=None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self, info):
        new_Node = Node(info)
        if self.head != None:
            new_Node.link = self.head
            self.head = new_Node
        else:
            self.head = new_Node
        
    def insert_at_end(self, info):
        new_Node = Node(info)
        if self.head !=None:
            current = self.head
            while current.link !=None:
                current = current.link
            current.link = new_Node
        else:
            self.head = new_Node

    def insert_at_given_node(self,info,item):
        if self.head != None:
            current = self.head
            while current.link != None:
                if current.info == item:
                    new_Node = Node(info)
                    new_Node.link = current.link #current nxt links to new's link
                    current.link = new_Node#and new links to current
                current = current.link

    def display(self):
        current = self.head
        while current != None :
            print(current.info)
            current = current.link
    
    def kthfromlast_1(self,k):#o(n),o(1) and 2 traversals
        n=0
        current = self.head
        while current.link != None:
            n+=1
            current = current.link
        x = (n-k+1)
        pos=0
        current = self.head
        while current != None:
            if pos == x:
                print(current.info)
            current = current.link
            pos+=1

    def kthfromlast_2(self,k):
        pos=1
        q=self.head
        p=self.head
        while q.link != None:
            if pos>=k :#it starts when q reaches k
                p = p.link
                q = q.link
            else:
                q=q.link#until q reaches k
            pos+=1
        return p.info
        

LL = LinkedList()
LL.insert_at_begining(10)
LL.insert_at_begining(13)
LL.display()
print("___________")
LL.insert_at_end(22)
LL.insert_at_end(44)
LL.display()
print("_______")
LL.insert_at_given_node(11,22)
LL.display()
print("__________")
LL.kthfromlast_1(3)
print(LL.kthfromlast_2(2))
