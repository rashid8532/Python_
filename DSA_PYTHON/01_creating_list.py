import ctypes
class Meralist:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__CreateArray(self.size)

    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return "Empty list"
        
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1
    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__CreateArray(new_capacity)
        self.size = new_capacity
        # copy the content of A to B 
        for i in range(self.n):
            B[i] = self.A[i]
        # reasign B to A
        self.A = B
    
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i 
        return "value Error item not found "
    
    def insert(self,idx,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,idx,-1):
            self.A[i] = self.A[i-1]
        
        self.A[idx] = item
        self.n = self.n + 1
    
    def remove(self,pos):
        # to find the elements 
        pos = self.find(pos)
        # to delete tehe element
        if type(pos) == int:
            self.__delitem__(pos)
        else :
            return pos


    def __delitem__(self, idx):
        if 0 <= idx > self.n :
            print("error")
            return 
        for i in range(idx,self.n-1,1):
            self.A[i] = self.A[i+1]
        self.n = self.n-1


    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] +']'
    

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else :
            return "index out of bound error"

    def __CreateArray(self,capacity):
        # this code creates a c type array(static , referential) with size capacity 
        return (capacity*ctypes.py_object)()
    
L = Meralist()
L.append(3)
L.append(4)
L.append(5)
L.append(5)
print(L)
L.insert(2,8)
print(L)
# del L[2]
L.remove(3)
print(L)

# print(L.find(5))

# a = [10,20,30,40,50]
# print(a)
# a.insert(2,25)
# print(a)
