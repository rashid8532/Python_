class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Empty linkedlist 
        self.head = None
        self.n = 0 
    def __len__(self):
        return self.n
    
    def insert_head(self, value):
        # Creating the new node
        new_node = Node(value)

        # connecting the new node with head 
        new_node.next = self.head

        # assigning the new node as a head 
        self.head = new_node

        # increment n
        self.n = self.n + 1

    def __str__(self):
        curr = self.head
        
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
        
        curr = self.head
        while curr.next != None:
            curr = curr.next 
        
        # you are at last node now 
        curr.next = new_node
        self.n = self.n + 1 
    
    def insert_after(self,item,value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == item:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else :
            return "Item not found"
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return "empty Linked List"
        self.head = self.head.next
        self.n = self.n-1

    def delete_tail(self):
        curr = self.head
        if self.head==None:
            return "Empty list"
        if curr.next == None:
            self.delete_head()
        if self.head == None:
            return "empty LL"
        
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n-1
    
    def remove(self,value):
        if self.head == None:
            print('Empty LL')
            return 'Empty LL'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        # if found 
        if curr.next == None:
            print("Not Found ")
            return 0
        else:
            curr.next = curr.next.next
    

    def find(self,value):
        if self.head == None:
            print("Empty LL")
            return "Empty LL"
        curr = self.head
        count = -1
        while curr != None:
            count = count + 1
            if curr.data == value:
                print("At the index of ", count)
                return count
            curr = curr.next
        print("Not found")

    
    def indexing(self,index):
        if index > self.n or index == None:
            print("Index out of bound")
            return 0
        if self.head == None:
            print("Empty LL")
            return 0 
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                print(curr.data)
                return 0 
            pos = pos + 1
            curr = curr.next
        
        

        
        
        


        

            




L = LinkedList()
# a = Node(1)
# b= Node(2)
# c = Node(3)

# print(a.next)

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append(8)
L.insert_after(1,200)
print(L)
# L.clear()
L.delete_tail()# this is a pop operation 
L.delete_tail()
L.delete_tail()
L.delete_tail()
L.delete_tail()
L.delete_tail()
print(L.delete_tail())
print(L)

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
# print(L)
# L.remove(2)
# L.remove(4)
# L.remove(3)
# L.remove(1)
# L.remove(1)

# print(L)
print(L)

L.indexing(55)