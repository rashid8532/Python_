marks = (93, 94, 95, 99, 99, 99,99)
## These Tupples are immutable 
marks[0] == 99
print(marks)

## Operations on the tupple 
## count 
print(marks.count(99))
## Index 
print(marks.index(95))


        #### SETS #####
marksSet = {93,94,95,95,95,95,99}
print("Set",marksSet)

for score in marksSet:
    print(score)

        #### Dictionary ####
markDictionary = {
    "english" : 96,
    "Maths" : 98,
    "physics" : 99,
}
markDictionary["Hindi"] = 90
print(markDictionary)