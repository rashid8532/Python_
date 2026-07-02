class Stack:
    def __init__(self,size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1
    
    def traverse(self):
        if self.top == -1 :
            print("Empty Stack ")
            return
        for i in range(self.size):
            print(self.__stack[i],end=" ")
    
    def push(self,value):
        if self.top == self.size - 1:
            print("Overflow")
        self.top += 1
        s.__stack[self.top] = value
    
    def peak(self):
        if self.top == -1:
            print("Empty Stack")
        print(self.__stack[self.top])
    
    def pop(self):
        if self.top == -1:
            print("Empty Stack")
            return
        data = self.__stack[self.top]
        print(data)
        self.__stack[self.top] = None
        self.top = self.top - 1 




s = Stack(3)
s.push(10)
s.push(20)
s.push(30)

# s.traverse()

s.peak()



s.traverse()