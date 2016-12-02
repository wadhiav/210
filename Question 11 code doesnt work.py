class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None
 
class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))

    def delete_node(self,rem): # rem = remove
        while n!=None:
            n=self.head # n is the start
            if n.value==rem:
                if n.next==None: # if there is no next node moves to the previous one
                    n.next.prev=None # moves backwards
                    self.tail=n.prev # if it has reached the end, previouses
                elif n.prev==None: # gone back to start
                    self.head=n.next#
                    
            else:
                n.next.prev=n.next
                n.prev.next=n.prev
                print("node deleted")

         
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.display()
    rem = input("which node would you like to remove: ")
    l.delete_node(rem)
    l.display()
