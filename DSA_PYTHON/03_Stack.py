class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack :
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None

    def peak(self):
        if self.top == None:
            print("Stack is empty")
        else :
            print(self.top.data)

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top == None:
            print("stack is empty")
        else:
            self.top = self.top.next
    
    def treverse(self):
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    def size(self):
        c = 0 
        curr =  self.top 
        while curr != None:
            # print(c)
            c = c + 1
            curr = curr.next
        print(c)

S = Stack()
S.push(10)
S.push(10)
S.push(10)
S.push(10)
S.push(10)
S.push(20)
S.push(30)
S.push(40)
# print(S)
# S.pop()
S.treverse()
# S.size()
S.peak()