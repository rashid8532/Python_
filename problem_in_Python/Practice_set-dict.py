dictionary = {}
dictionary["cat"] = "a small animal"
dictionary["table"] = ["a piece of furniture","list of facts & figures"]
print(dictionary)
print(type(dictionary["table"]))

# Find the total no. of class room 
subject = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print("We need the ",len(subject)," class rooms")

marks = {}
n = int(input("The no. of sub : "))
for i in range(n):
    x = input("write down the subject : ")
    y = int(input("write down the marks : "))
    marks.update({x : y})

print(marks)