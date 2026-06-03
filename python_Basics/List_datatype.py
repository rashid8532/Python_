marks = [90,98,94]
# print(marks[0])
# print(marks[1])
# print(marks[-1])# minus in array is used for the start from the last index 
# # To make a sub list 
# print(marks[0:2])# output would be [90,98]

# List whith the for loop 

for i in marks:
    print(i)

# Important operations on a list

## This is to add the item in the list at last 
marks.append(99)
print(marks)

## this adds an element at any point 
marks.insert(1,100)
print(marks)

## trevarsal on the list by while loop 
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

# ## Clear operation 
# marks.clear()
# print(marks)

## Remove something 
marks.remove(100)
print(marks)


## Break and continue in the python 
School = ["Rashid", "Anwar","Akmal","Amir"]
for student in School:
    if student == "Akmal":
        continue
    else:
        print(student)

names = ["Rashid" , "Anwar" , "Akmal" , "Aqdas"]

nu = [1,2,5,3,6,1,2,22,4,23,54,26,34,23,12]
print(len(nu))
nu1 = sorted(nu)
print(nu1)
print(nu.sort(reverse=True))# This is for reverse but it does not print anything
print(nu)
nu.sort() # This sort for accending order 
print(nu)
