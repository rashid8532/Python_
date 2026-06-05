# # enumerate operation in list 
# list1 = [1,2,5,3,65,5,332,765,6,543,26,54]
# for i in enumerate(list1) :
#     print(i)# it prints everithing with the index 

Mn = int(input("Enter the operation number: "))
name = []
result = []
for l in range(Mn) :
        name = input("Enter the Input : ").split()
        if name[0] == "append":
            j = int(name[1])
            result.append(j)
        elif name[0] == "remove":
            j = int(name[1])
            result.remove(j)
        elif name[0] == "insert":
            j = int(name[1])
            k = int(name[2])
            result.insert(j , k)
        elif name[0] == "print":
            print(result)
        elif name[0] == "sort":
            result.sort()
        elif name[0] == "pop":
            result.pop()
        elif name[0] == "reverse":
            result.reverse()



    