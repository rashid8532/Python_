class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else :
            self.rear.next = new_node
            self.rear = new_node 
    
    def dequeue(self):
        if self.front == None:
            print("Empty queue")
            return
        else:
            self.front = self.front.next

    def traverse(self):
        curr  = self.front
        while curr != None:
            print(curr.data,end=" ")
            curr = curr.next


q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.traverse()

# https://shajarcloudnebula.atlassian.net/wiki/spaces/I2/pages/edit-v2/4751362?draftShareId=34925026-bd0b-41f8-998e-e4dee2cde0ac