info = {
    "name" : "Rashid",
    "mentor" : "Shajar sir ",
    "age" : 21,
    "position" : "Intern"
}
info['age'] = 23
print(info["age"])
## Nested dictionry 
student ={
    "name" : "Rashid",
    "subjects" : {
        "maths" : 68,
        "A/c" : 78,
        "CA" : 91,
    }
}

print(student["subjects"]['CA'])


## Methods of dictionary 
print(student.keys())## return all key
print(student.values())## return all values 
print(student.items())## return all key, and value pairs 
print(student.get('name'))## return the item without error 
student.update({"city" : "delhi"})## update item without error
print(student)
student.pop('name')## remove the that we gave
print(student)
student.update({"city" : "lucknow"}) 
print(student)
student.popitem()## removes last item 
print(student)
## student.clear() ## clear hole dictionary
new_student = student.copy()## copy hole dictionary into the new
print(new_student)

student.setdefault('age',21)##Returns the value if key exists; otherwise inserts the key with a default value.
print(student)

di = {}
di["1"] = 1
di["1"] = 1
print(di)