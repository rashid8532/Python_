## del keyword 
class Car :
    def __init__(self,type):
        self.type = type
        
    name = "Car"

class Company(Car):
    def __init__(self ,company,type):
        self.company = company
        super().__init__(type)
    @classmethod
    def changeName(cls,name):
        cls.name = name

c1 = Company("TATA","EV")
# del c1    
print(c1.company)
# @property this is used for changing function in class
